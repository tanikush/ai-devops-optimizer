import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import joblib
import os

class TimeEstimator:
    def __init__(self, model_path=None):
        self.model = None
        self.model_path = model_path
        if model_path and os.path.exists(model_path):
            self.load_model(model_path)
        else:
            self.model = GradientBoostingRegressor(n_estimators=100, random_state=42)
    
    def prepare_features(self, build_data):
        """Extract features from build data"""
        features = []
        
        # Code metrics
        features.append(build_data.get('files_changed', 0))
        features.append(build_data.get('lines_added', 0))
        features.append(build_data.get('lines_deleted', 0))
        
        # Test metrics
        features.append(build_data.get('test_count', 0))
        features.append(build_data.get('test_files', 0))
        
        # Dependencies
        features.append(build_data.get('dependency_count', 10))
        features.append(build_data.get('new_dependencies', 0))
        
        # Historical average
        features.append(build_data.get('avg_duration_last_10', 300))
        
        # Build type
        features.append(1 if build_data.get('is_pull_request') else 0)
        
        # Resource allocation
        features.append(build_data.get('cpu_cores', 2))
        features.append(build_data.get('memory_gb', 4))
        
        return np.array(features).reshape(1, -1)
    
    def predict(self, build_data):
        """Predict build duration"""
        if self.model is None:
            # Return dummy prediction if model not trained
            avg_duration = build_data.get('avg_duration_last_10', 300)
            return {
                'estimated_duration': avg_duration,
                'confidence_interval': {
                    'min': avg_duration * 0.85,
                    'max': avg_duration * 1.15
                }
            }
        
        features = self.prepare_features(build_data)
        prediction = self.model.predict(features)[0]
        
        # Calculate confidence interval (simplified)
        confidence_range = prediction * 0.15
        
        return {
            'estimated_duration': float(prediction),
            'confidence_interval': {
                'min': float(prediction - confidence_range),
                'max': float(prediction + confidence_range)
            }
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
