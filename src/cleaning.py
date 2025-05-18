import pandas as pd 
import numpy as np

class DataCleaning:
    
    def __init__(self, df):
        self.df = df
        
    @staticmethod 
    def clean_data(self):
        
        
        """Cleans the data by removing duplicates and resetting the index."""
        
        self.df.drop_duplicates(inplace=True)
        self.df.reset_index(drop=True, inplace=True)
        return self

    @staticmethod
    def handle_missing_values(self, df: pd.DataFrame, columns: list, method: str = 'median'):
        
        """
        Handles missing values in the DataFrame.

        Args:
            df (pd.DataFrame): DataFrame to handle missing values.
            columns (list): List of columns to check for missing values.
            method (str): Method to handle missing values. Options are 'drop', 'mean', 'median', 'mode'.
        
        Returns:
            pd.DataFrame: DataFrame with handled missing values.
        """
        
        if method == 'drop':
            self.df.dropna(subset=columns, inplace=True)
        elif method == 'mean':
            self.df[columns] = self.df[columns].fillna(self.df[columns].mean())
        elif method == 'median':
            self.df[columns] = self.df[columns].fillna(self.df[columns].median())
        elif method == 'mode':
            self.df[columns] = self.df[columns].fillna(self.df[columns].mode().iloc[0])
        else:
            raise ValueError("Method not recognized. Use 'drop', 'mean', 'median', or 'mode'.")
        
        return self

    
    def handle_outliers(self, columns: list, z_threshold=3):
        
        """
        Flags and removes outliers in the specified columns using Z-score method.

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
        for column in columns:
            self.df[column] = self.df[column].fillna(self.df[column].median())
        return self
   