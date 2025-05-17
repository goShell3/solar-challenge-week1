import pandas as pd
import numpy as np

class SolarDatacleaner:
    
    def __init__(self, df):
        self.df = df.copy()
        self.outlier_flags = None 
        
    def handle_missing_values(self, max_null_percentage=5):
        """
            Drop columens exceeding 
            null threshold
        """
        threshold = len(self.df) * (max_null_percentage / 100)
        self.df = self.df.dropna(thresh=threshold, axis=1, inplace=True)
        return self
    
    def handle_outliers(self, columns, z_threshold=3):
        """Flags and removes outliers in the specified columns using Z-score method.

        Args:
            columns (_type_): _description_
            z_threshold (int, optional): _description_. Defaults to 3.
            
        """
        
        z_scores = (self.df[columns] - self.df[columns].mean()) / self.df[columns].std()
        self.outliner_flags = z_scores.abs() > z_threshold
        self.df = self.df[~self.outliner_flags.any(axis=1)]
        return self
    
    def impute_median(self, columns):
        """Imputes missing values with the median of the column.

        Args:
            columns (_type_): _description_
        """
        self.df[columns] = self.df[columns].fillna(self.df[columns].median())
        return self
        