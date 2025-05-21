"""
Solar Data Analysis Package

A comprehensive toolkit for analyzing solar performance data including:
- Time series analysis of GHI, DNI, DHI, and temperature
- Cleaning impact assessment
- Correlation and relationship analysis
- Wind distribution analysis
- Temperature and humidity effects

Example usage:
>>> from solar_analysis import (
...     plot_daily_patterns,
...     plot_cleaning_impact,
...     plot_wind_rose
... )
"""

from .time_series import (
    plot_daily_patterns,
    plot_seasonal_trends,
    detect_anomalies
)

from .cleaning_impact import (
    plot_cleaning_impact,
    plot_cleaning_timeseries
)

from .correlation_analysis import (
    plot_correlation_heatmap,
    plot_scatter_relationships
)

from .wind_analysis import (
    plot_wind_rose,
    plot_wind_distributions,
    plot_ghi_histogram
)

from .temperature_analysis import (
    plot_rh_temperature_relationship,
    plot_bubble_chart
)

# Define what gets imported with 'from solar_analysis import *'
__all__ = [
    # Time series
    'plot_daily_patterns',
    'plot_seasonal_trends',
    'detect_anomalies',
    
    # Cleaning impact
    'plot_cleaning_impact',
    'plot_cleaning_timeseries',
    
    # Correlation
    'plot_correlation_heatmap',
    'plot_scatter_relationships',
    
    # Wind analysis
    'plot_wind_rose',
    'plot_wind_distributions',
    'plot_ghi_histogram',
    
    # Temperature analysis
    'plot_rh_temperature_relationship',
    'plot_bubble_chart'
]