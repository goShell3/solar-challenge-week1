import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

class TimeFeatureExtractor(BaseEstimator, TransformerMixin):
    """Extracts time-based features from timestamps"""
    def __init__(self):
        self.feature_names = ['hour_sin', 'hour_cos', 'month_sin', 'month_cos']
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        if isinstance(X, pd.DataFrame):
            timestamps = X.index
        else:
            timestamps = pd.to_datetime(X)
            
        hour = timestamps.hour
        month = timestamps.month
        
        return np.column_stack([
            np.sin(2 * np.pi * hour/24),
            np.cos(2 * np.pi * hour/24),
            np.sin(2 * np.pi * month/12),
            np.cos(2 * np.pi * month/12)
        ])
    
    # Backward-compatible feature names method
    def get_feature_names(self):
        return self.feature_names
    
    # For newer scikit-learn versions
    def get_feature_names_out(self, input_features=None):
        return self.feature_names

class SolarFeatureGenerator:
    """Generates solar-specific features"""
    def __init__(self, params):
        self.params = params
        self.feature_names = []
        
    def create_pipeline(self):
        """Create feature engineering pipeline"""
        return Pipeline([
            ('time_features', TimeFeatureExtractor()),
            ('scaler', StandardScaler())
        ])
    
    def generate_features(self, df):
        
        """
            Generate all features
        """
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")
            
        if not isinstance(df.index, pd.DatetimeIndex):
            raise ValueError("DataFrame index must be a DatetimeIndex")
        
        # Time-based features
        pipeline = self.create_pipeline()
        time_features = pipeline.fit_transform(df)
        
        # Get feature names in a backward-compatible way
        time_extractor = pipeline.named_steps['time_features']
        if hasattr(time_extractor, 'get_feature_names_out'):
            time_feature_names = time_extractor.get_feature_names_out()
        elif hasattr(time_extractor, 'get_feature_names'):
            time_feature_names = time_extractor.get_feature_names()
        else:
            time_feature_names = ['hour_sin', 'hour_cos', 'month_sin', 'month_cos']
            
        self.feature_names.extend(time_feature_names)
        
        # Radiation features
        df['clearness_index'] = df['GHI'] / (df['DNI'] + 1e-6)
        self.feature_names.append('clearness_index')
        
        # Weather features
        if 'Tamb' in df.columns and 'RH' in df.columns:
            df['heat_index'] = 0.5 * (df['Tamb'] + 61.0 + (df['Tamb']-68)*1.2 + df['RH']*0.094)
            self.feature_names.append('heat_index')
        
        # Combine all features
        features = [time_features]
        features.append(df[['clearness_index']].values)
        
        if 'heat_index' in df.columns:
            features.append(df[['heat_index']].values)
        
        return np.hstack(features)