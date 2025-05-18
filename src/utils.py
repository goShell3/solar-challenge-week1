import sys
import os

class Utils:
    
    def __init__(self, df):
        
        self.df = df 
        
    @staticmethod
    def export_clean_csv(df, country):
        
        """Exports the cleaned DataFrame to a CSV file.
        1. The file is saved in the 'data' directory.
        2. The filename is formatted as '{country}_clean.csv'.
        3. The index is not included in the CSV file.
        

        Args:
            df (dataframe): the dataframe to be exported
            country (str): the country name to be used in the filename
        """
        
        df.to_csv(f"../data/{country}_clean.csv", index=False)
        
    