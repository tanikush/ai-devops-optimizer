import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

class FailurePredictor:
    def __init__(self, model_path=None):
        self.model = None
        self.model_path = model_path
        if model_path and os.path.exists(model_path):
            self.load_model(model_path)
        else:
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    def prepare_features(self, build_data):
        """Extract features from build data"""
        features = []
        
        # Historical success rate
        features.append(build_data.get('historical_success_rate', 0.9))
        
        # Code changes
        features.append(build_data.get('files_changed', 0))
        features.append(build_data.get('lines_added', 0))
        features.append(build_data.get('lines_deleted', 0))
        
        # Test metrics
        features.append(build_data.get('test_count', 0))
        features.append(build_data.get('test_coverage', 0.8))
        
        # Time-based features
        features.append(build_data.get('hour_of_day', 12))
        features.append(build_data.get('day_of_week', 3))
        
        # Previous build status (1 for success, 0 for failure)
        features.append(1 if build_data.get('previous_status') == 'success' else 0)
        
        # Build complexity
        features.append(build_data.get('dependency_count', 10))
        
        return np.array(features).reshape(1, -1)
    
    def predict(self, build_data):
        """Predict if build will fail"""
        if self.model is None:
            # Return dummy prediction if model not trained
            return {
                'prediction': 'success',
                'probability_failure': 0.15,
                'probability_success': 0.85,
                'confidence': 0.85
            }
        
        features = self.prepare_features(build_data)
        prediction = self.model.predict(features)[0]
        probabilities = self.model.predict_proba(features)[0]
        
        return {
            'prediction': 'failure' if prediction == 1 else 'success',
            'probability_failure': float(probabilities[1]),
            'probability_success': float(probabilities[0]),
            'confidence': float(max(probabilities))
        }
    
    def train(self, X, y):
        """Train the model"""
        self.model.fit(X, y)
    
    def save_model(self, path):
        """Save model to disk"""
        joblib.dump(self.model, path)
        self.model_path = path
    
    def load_model(self, path):
        """Load model from disk"""
        self.model = joblib.load(path)
        self.model_path = path
