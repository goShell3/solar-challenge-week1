#!/usr/bin/env python3
"""
Usage: python run_eda_pipeline.py <country> <raw_data_path>
Example: python run_eda_pipeline.py benin ../data/benin_raw.csv
"""

import sys
import pandas as pd
from src.data_cleaner import SolarDataCleaner
from src.visualization import SolarVisualizer

def main(country, input_path):
    # Load and clean data
    df = pd.read_csv(input_path)
    cleaner = (SolarDataCleaner(df)
              .handle_missing_values()
              .remove_outliers_zscore(['GHI','DNI','DHI'])
              .impute_median(['Tamb','WS']))
    
    # Generate plots
    plots = [
        SolarVisualizer.plot_time_series(cleaner.df, 'Timestamp', 'GHI'),
        SolarVisualizer.plot_correlation_heatmap(cleaner.df, ['GHI','DNI','Tamb'])
    ]
    
    # Save outputs
    cleaner.df.to_csv(f'../data/{country}_clean.csv', index=False)
    for i, plot in enumerate(plots):
        plot.savefig(f'../figures/{country}_plot_{i}.png')
    
    print(f"EDA completed for {country}. Outputs saved.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])