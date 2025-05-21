import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_daily_patterns(df, variables=['GHI', 'DNI', 'DHI', 'Tamb']):
    """Plot daily patterns for specified variables"""
    plt.figure(figsize=(15, 10))
    for i, var in enumerate(variables, 1):
        plt.subplot(2, 2, i)
        sns.boxplot(x='Hour', y=var, data=df)
        plt.title(f'Hourly {var} Distribution')
    plt.tight_layout()
    return plt

def plot_seasonal_trends(df, variables=['GHI', 'DNI', 'DHI', 'Tamb'], window=24*30):
    """Plot rolling average seasonal trends"""
    plt.figure(figsize=(15, 8))
    for var in variables:
        df[var].rolling(window).mean().plot(label=f'{var} ({window//24}-day avg)')
    plt.title('Seasonal Trends')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    return plt

def detect_anomalies(df, variable='GHI', threshold=1000):
    """Detect and plot anomalies based on threshold"""
    plt.figure(figsize=(15, 5))
    plt.plot(df.index, df[variable], label=variable, alpha=0.7)
    anomalies = df[variable] > threshold
    plt.scatter(df.index[anomalies], df[variable][anomalies], 
               color='red', label=f'Anomalies (> {threshold})')
    plt.title(f'{variable} Anomaly Detection')
    plt.ylabel(variable)
    plt.legend()
    plt.grid(True)
    return plt