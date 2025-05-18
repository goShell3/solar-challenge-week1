import pandas as pd
import numpy as np
# from sklearn.base  import BaseEstimator, TransformerMixin


class SolarFeatureEngineering:
    """
    A class for feature engineering on solar energy data.
    """

    def __init__(self, df):
        self.df = df

    def add_time_features(self):
        self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'])
        self.df['hour'] = self.df['Timestamp'].dt.hour
        self.df['day_of_week'] = self.df['Timestamp'].dt.dayofweek
        self.df['day_of_year'] = self.df['Timestamp'].dt.dayofyear
        self.df['month'] =self.df['Timestamp'].dt.month
        self.df['week_of_year'] = self.df['Timestamp'].dt.isocalendar().week
        self.df['is_weekend'] = self.df['day_of_week'].isin([5,6]).astype(int)
        self.df['season'] = (self.df['month']%12 + 3)//3  # 1=winter, 2=spring, etc.
        self.df['solar_time'] = self.df['hour'] + (self.df['Timestamp'].dt.longitude/15)
        
        return self.df
    
    # solar position feature 
    
    def add_solar_position_features(self):
        pass 
    
    # Rolling weather features
    def add_rolling_weather_features(self, window_size=24):
        """
        Adds rolling mean and standard deviation features for weather data.
        
        Args:
            window_size (int): Size of the rolling window.
        
        Returns:
            pd.DataFrame: DataFrame with rolling features added.
        """
        weather_columns = ['Temperature', 'Humidity', 'WindSpeed']
        
        for col in weather_columns:
            self.df[f'{col}_rolling_mean'] = self.df[col].rolling(window=window_size).mean()
            self.df[f'{col}_rolling_std'] = self.df[col].rolling(window=window_size).std()
        
        return self.df
    
    
    # temprature_feature
    def add_temperature_features(self):
        """
        Adds temperature-related features to the DataFrame.
        
        Returns:
            pd.DataFrame: DataFrame with temperature features added.
        """
        # Temperature differentials
        self.df['TModA_amb_diff'] = self.df['TModA'] - self.df['Tamb']
        self.df['TModA_amb_diff'] = self.df['TModA'] - self.df['Tamb']
        self.df['TModB_amb_diff'] = self.df['TModB'] - self.df['Tamb']

        # Temperature effects
        self.df['TModA_effect'] = np.where(self.df['TModA_amb_diff'] > 0, 1, 0)
        self.df['temp_effect_A'] = self.df['ModA'] * (1 - 0.005*(self.df['TModA'] -25))
        
        return self.df
    
    
    def add_solar_position_features(self, latitude, longitude):
        """
        Adds solar position features using pysolar.
        
        Args:
            latitude (float): Site latitude
            longitude (float): Site longitude
            
        Returns:
            pd.DataFrame: DataFrame with solar position features added
        """
        from pysolar.solar import get_altitude, get_azimuth
        from datetime import timezone
        
        def calculate_solar_features(timestamp):
            try:
                altitude = get_altitude(latitude, longitude, timestamp.replace(tzinfo=timezone.utc))
                azimuth = get_azimuth(latitude, longitude, timestamp.replace(tzinfo=timezone.utc))
                return pd.Series([altitude, azimuth])
            except:
                return pd.Series([np.nan, np.nan])
        
        solar_pos = self.df['Timestamp'].apply(calculate_solar_features)
        self.df['solar_altitude'] = solar_pos[0]
        self.df['solar_azimuth'] = solar_pos[1]
        self.df['solar_zenith'] = 90 - self.df['solar_altitude']
        
        return self.df