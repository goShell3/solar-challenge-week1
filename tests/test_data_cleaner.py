import pytest
import pandas as pd
import numpy as np
from ..src.data.cleaning import DataCleaning

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'GHI': [1000, 950, 1200, 50, 3000],  # 3000 and 50 are outliers
        'Tamb': [25, 24, None, 26, 25]
    })

def test_outlier_removal(sample_data):
    cleaner = DataCleaning(sample_data).remove_outliers_zscore(['GHI'])
    assert len(cleaner.df) == 3  # Should remove 2 outliers

def test_missing_value_handling(sample_data):
    cleaner = DataCleaning(sample_data).impute_median(['Tamb'])
    assert cleaner.df['Tamb'].isna().sum() == 0