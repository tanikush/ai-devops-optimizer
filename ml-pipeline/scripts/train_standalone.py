import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
from sklearn.metrics import accuracy_score, classification_report, mean_absolute_error
import joblib
import os

print("=" * 60)
print("🤖 AI-Powered DevOps Pipeline Optimizer")
print("ML Model Training Script")
print("=" * 60)
print()

def generate_sample_data(n_samples=1000):
    """Generate sample training data for pipeline builds"""
    print(f"📊 Generating {n_samples} sample data points...")
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
    
    # Generate target: failure = 1, success = 0
    # Lower success rate + previous failure + more changes = higher failure probability
    failure_prob = (
        (1 - df['historical_success_rate']) * 0.5 +
        (1 - df['previous_status']) * 0.3 +
        (df['files_changed'] / 100) * 0.2
    )
    
    df['failed'] = (np.random.random(n_samples) < failure_prob).astype(int)
    
    # Generate duration target (in seconds)
    df['duration'] = (
        df['files_changed'] * 2 +
        df['test_count'] * 1.5 +
        df['dependency_count'] * 3 +
        np.random.normal(0, 20, n_samples)
    ).clip(60, 1000)
    
    print(f"✅ Generated {len(df)} samples")
    print(f"   - Failed builds: {df['failed'].sum()} ({df['failed'].mean()*100:.1f}%)")
    print(f"   - Successful builds: {(1-df['failed']).sum()} ({(1-df['failed']).mean()*100:.1f}%)")
    print()
    
    return df

def train_failure_predictor(df):
    """Train the failure prediction model"""
    print("🎯 Training Failure Prediction Model...")
    print("-" * 60)
    
    # Prepare features and target
    feature_cols = [
        'historical_success_rate', 'files_changed', 'lines_added', 
        'lines_deleted', 'test_count', 'test_coverage', 'hour_of_day',
        'day_of_week', 'previous_status', 'dependency_count'
    ]
    
    X = df[feature_cols].values
    y = df['failed'].values
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    print()
    
    # Train model
    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n✅ Model Training Complete!")
    print(f"Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Success', 'Failure']))
    
    # Save model
    model_dir = '../models'
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, 'failure_predictor.pkl')
    joblib.dump(model, model_path)
    print(f"\n💾 Model saved to: {model_path}")
    print()
    
    return model, accuracy

def train_time_estimator(df):
    """Train the duration estimation model"""
    print("⏱️  Training Build Duration Estimation Model...")
    print("-" * 60)
    
    # Prepare features and target
    feature_cols = [
        'files_changed', 'lines_added', 'lines_deleted', 
        'test_count', 'dependency_count'
    ]
    
    X = df[feature_cols].values
    y = df['duration'].values
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    print()
    
    # Train model
    print("Training Gradient Boosting Regressor...")
    model = GradientBoostingRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(np.mean((y_test - y_pred) ** 2))
    
    print(f"\n✅ Model Training Complete!")
    print(f"Mean Absolute Error (MAE): {mae:.2f} seconds")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f} seconds")
    print(f"Average actual duration: {y_test.mean():.2f} seconds")
    print(f"Average predicted duration: {y_pred.mean():.2f} seconds")
    
    # Save model
    model_dir = '../models'
    model_path = os.path.join(model_dir, 'time_estimator.pkl')
    joblib.dump(model, model_path)
    print(f"\n💾 Model saved to: {model_path}")
    print()
    
    return model, mae

def main():
    print("Starting ML Model Training Pipeline...\n")
    
    # Generate data
    df = generate_sample_data(1000)
    
    # Save sample data
    data_dir = '../data/processed'
    os.makedirs(data_dir, exist_ok=True)
    data_path = os.path.join(data_dir, 'training_data.csv')
    df.to_csv(data_path, index=False)
    print(f"💾 Training data saved to: {data_path}\n")
    
    # Train models
    failure_model, failure_accuracy = train_failure_predictor(df)
    time_model, time_mae = train_time_estimator(df)
    
    # Summary
    print("=" * 60)
    print("🎉 Training Complete! Summary:")
    print("=" * 60)
    print(f"✅ Failure Prediction Model: {failure_accuracy*100:.2f}% accuracy")
    print(f"✅ Duration Estimation Model: {time_mae:.2f}s MAE")
    print(f"\n📁 Models saved in: ml-pipeline/models/")
    print(f"   - failure_predictor.pkl")
    print(f"   - time_estimator.pkl")
    print(f"\n📊 Training data saved in: ml-pipeline/data/processed/")
    print(f"   - training_data.csv")
    print("\n🚀 You can now use these models in your backend API!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
