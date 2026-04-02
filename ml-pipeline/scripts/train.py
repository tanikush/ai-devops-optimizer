import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app.ml.models.failure_predictor import FailurePredictor
from backend.app.ml.models.time_estimator import TimeEstimator

def generate_sample_data(n_samples=1000):
    """Generate sample training data"""
    np.random.seed(42)
    
    data = {
        'historical_success_rate': np.random.uniform(0.7, 1.0, n_samples),
        'files_changed': np.random.randint(1, 50, n_samples),
        'lines_added': np.random.randint(10, 500, n_samples),
        'lines_deleted': np.random.randint(5, 300, n_samples),
        'test_count': np.random.randint(10, 200, n_samples),
        'test_coverage': np.random.uniform(0.5, 1.0, n_samples),
        'hour_of_day': np.random.randint(0, 24, n_samples),
        'day_of_week': np.random.randint(0, 7, n_samples),
        'previous_status': np.random.choice([0, 1], n_samples, p=[0.1, 0.9]),
        'dependency_count': np.random.randint(5, 50, n_samples),
    }
    
    df = pd.DataFrame(data)
    
    # Generate target (failure = 1, success = 0)
    # Higher success rate and previous success -> lower failure probability
    failure_prob = (1 - df['historical_success_rate']) * 0.5 + \
                   (1 - df['previous_status']) * 0.3 + \
                   (df['files_changed'] / 100) * 0.2
    
    df['failed'] = (np.random.random(n_samples) < failure_prob).astype(int)
    
    # Generate duration target
    df['duration'] = (
        df['files_changed'] * 2 +
        df['test_count'] * 1.5 +
        df['dependency_count'] * 3 +
        np.random.normal(0, 20, n_samples)
    ).clip(60, 1000)
    
    return df

def train_failure_predictor():
    """Train the failure prediction model"""
    print("Training Failure Predictor...")
    
    # Generate data
    df = generate_sample_data(1000)
    
    # Prepare features and target
    feature_cols = ['historical_success_rate', 'files_changed', 'lines_added', 
                   'lines_deleted', 'test_count', 'test_coverage', 'hour_of_day',
                   'day_of_week', 'previous_status', 'dependency_count']
    
    X = df[feature_cols].values
    y = df['failed'].values
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    predictor = FailurePredictor()
    predictor.train(X_train, y_train)
    
    # Evaluate
    y_pred = predictor.model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save model
    model_path = '../ml-pipeline/models/failure_predictor.pkl'
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    predictor.save_model(model_path)
    print(f"\nModel saved to {model_path}")

def train_time_estimator():
    """Train the duration estimation model"""
    print("\nTraining Time Estimator...")
    
    # Generate data
    df = generate_sample_data(1000)
    
    # Prepare features and target
    feature_cols = ['files_changed', 'lines_added', 'lines_deleted', 'test_count',
                   'test_count', 'dependency_count', 'dependency_count',
                   'duration', 'previous_status', 'dependency_count', 'dependency_count']
    
    # Simplified features for time estimation
    X = df[['files_changed', 'lines_added', 'lines_deleted', 'test_count', 
            'dependency_count']].values
    # Add some derived features
    X = np.column_hstack([X, X[:, 3:4], np.zeros((X.shape[0], 1)), 
                          df['duration'].values.reshape(-1, 1), 
                          df['previous_status'].values.reshape(-1, 1),
                          X[:, 4:5], X[:, 4:5]])
    
    y = df['duration'].values
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    estimator = TimeEstimator()
    estimator.train(X_train, y_train)
    
    # Evaluate
    y_pred = estimator.model.predict(X_test)
    mae = np.mean(np.abs(y_test - y_pred))
    rmse = np.sqrt(np.mean((y_test - y_pred) ** 2))
    
    print(f"MAE: {mae:.2f} seconds")
    print(f"RMSE: {rmse:.2f} seconds")
    
    # Save model
    model_path = '../ml-pipeline/models/time_estimator.pkl'
    estimator.save_model(model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    print("Starting ML Model Training...\n")
    train_failure_predictor()
    train_time_estimator()
    print("\nTraining completed!")
