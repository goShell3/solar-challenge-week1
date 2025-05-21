import pandas as pd
import numpy as np
from typing import List, Union, Optional

class SolarDataCleaner:
    """A comprehensive data cleaning pipeline for solar energy datasets"""
    
    def __init__(self, df: pd.DataFrame):
        """
        Initialize the cleaner with a copy of the dataframe
        
        Args:
            df: Input solar data DataFrame with Timestamp index
        """
        self.df = df.copy()
        self.outlier_flags = None
        self.cleaning_report = {}
        
    # def handle_missing_values(self, max_null_percentage: float = 5.0) -> 'SolarDataCleaner':
    #     """
    #     Handle missing values by either dropping or interpolating
        
    #     Args:
    #         max_null_percentage: Maximum allowed percentage of nulls in a column
            
    #     Returns:
    #         self for method chaining
    #     """
    #     # Calculate threshold for dropping columns
    #     threshold = len(self.df) * (max_null_percentage / 100)
        
    #     # Before dropping columns
    #     original_cols = set(self.df.columns)
        
    #     # Drop columns with too many nulls
    #     self.df = self.df.dropna(axis=1, thresh=threshold)
        
    #     # Record dropped columns
    #     dropped_cols = original_cols - set(self.df.columns)
    #     if dropped_cols:
    #         self.cleaning_report['dropped_columns'] = list(dropped_cols)
        
    #     # Interpolate remaining missing values
    #     self.df = self.df.interpolate(method='time', limit_direction='both')
        
    #     # Fill any remaining nulls with median
    #     numeric_cols = self.df.select_dtypes(include=np.number).columns
    #     self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].median())
        
    #     return self
    
    def handle_missing_values(self, max_null_percentage=5):
    # Drop columns with too many nulls
        null_percent = self.df.isnull().mean() * 100
        dropped_cols = null_percent[null_percent > max_null_percentage].index
        self.df.drop(columns=dropped_cols, inplace=True)
        self.cleaning_report['dropped_columns'] = list(dropped_cols)

        # ✅ Ensure datetime index for time interpolation
        if not isinstance(self.df.index, pd.DatetimeIndex):
            if 'Timestamp' in self.df.columns:
                self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'])
                self.df.set_index('Timestamp', inplace=True)
            else:
                raise ValueError("DataFrame must have a datetime index or a 'Timestamp' column for time interpolation.")

        # Interpolate time-based missing values
        self.df = self.df.interpolate(method='time', limit_direction='both')

        # Fill any remaining nulls with median
        numeric_cols = self.df.select_dtypes(include=np.number).columns
        self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].median())

        return self

    
    def handle_outliers(self, columns: List[str], method: str = 'zscore', 
                       z_threshold: float = 3.0, iqr_factor: float = 1.5) -> 'SolarDataCleaner':
        """
        Identify and handle outliers using multiple methods
        
        Args:
            columns: List of columns to process
            method: 'zscore' or 'iqr'
            z_threshold: Threshold for z-score method
            iqr_factor: Multiplier for IQR method
            
        Returns:
            self for method chaining
        """
        if not isinstance(columns, list):
            columns = [columns]
            
        valid_methods = ['zscore', 'iqr']
        if method not in valid_methods:
            raise ValueError(f"Method must be one of {valid_methods}")
            
        outlier_mask = pd.Series(False, index=self.df.index)
        
        for col in columns:
            if col not in self.df.columns:
                continue
                
            if method == 'zscore':
                z_scores = (self.df[col] - self.df[col].mean()) / self.df[col].std()
                col_mask = z_scores.abs() > z_threshold
            else:  # IQR method
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                col_mask = (self.df[col] < (Q1 - iqr_factor * IQR)) | (self.df[col] > (Q3 + iqr_factor * IQR))
            
            outlier_mask |= col_mask
            
        self.outlier_flags = outlier_mask
        self.cleaning_report['outliers_removed'] = outlier_mask.sum()
        
        # Cap outliers instead of removing for time series continuity
        for col in columns:
            if method == 'zscore':
                upper_bound = self.df[col].mean() + z_threshold * self.df[col].std()
                lower_bound = self.df[col].mean() - z_threshold * self.df[col].std()
            else:
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                upper_bound = Q3 + iqr_factor * IQR
                lower_bound = Q1 - iqr_factor * IQR
                
            self.df[col] = np.where(self.df[col] > upper_bound, upper_bound, 
                                  np.where(self.df[col] < lower_bound, lower_bound, self.df[col]))
        
        return self
    
    def validate_physical_ranges(self) -> 'SolarDataCleaner':
        """
        Validate data against physical constraints for solar data
        
        Returns:
            self for method chaining
        """
        # GHI, DNI, DHI should be non-negative
        irradiance_cols = ['GHI', 'DNI', 'DHI']
        for col in irradiance_cols:
            if col in self.df.columns:
                self.df[col] = self.df[col].clip(lower=0)
                
        # Temperature realistic ranges (adjust as needed)
        if 'Tamb' in self.df.columns:
            self.df['Tamb'] = self.df['Tamb'].clip(lower=-40, upper=60)
            
        # Relative humidity 0-100%
        if 'RH' in self.df.columns:
            self.df['RH'] = self.df['RH'].clip(lower=0, upper=100)
            
        return self
    
    def add_time_features(self) -> 'SolarDataCleaner':
        """
        Add derived time features to the dataframe
        
        Returns:
            self for method chaining
        """
        if not isinstance(self.df.index, pd.DatetimeIndex):
            raise ValueError("Dataframe must have a DatetimeIndex")
            
        self.df['hour'] = self.df.index.hour
        self.df['month'] = self.df.index.month
        self.df['day_of_year'] = self.df.index.dayofyear
        
        # Cyclical features
        self.df['hour_sin'] = np.sin(2 * np.pi * self.df['hour']/24)
        self.df['hour_cos'] = np.cos(2 * np.pi * self.df['hour']/24)
        self.df['month_sin'] = np.sin(2 * np.pi * self.df['month']/12)
        self.df['month_cos'] = np.cos(2 * np.pi * self.df['month']/12)
        
        return self
    
    def get_cleaning_report(self) -> dict:
        """
        Get a report of all cleaning operations performed
        
        Returns:
            Dictionary containing cleaning statistics
        """
        return self.cleaning_report
    
    def get_clean_data(self) -> pd.DataFrame:
        """
        Return the cleaned dataframe
        
        Returns:
            Cleaned pandas DataFrame
        """
        return self.df.copy()