import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from windrose import WindroseAxes

def plot_wind_rose(df):
    """Plot wind rose using wind speed and direction"""
    ax = WindroseAxes.from_ax()
    ax.bar(df['WD'], df['WS'], normed=True, opening=0.8, edgecolor='white')
    ax.set_legend()
    plt.title('Wind Rose')
    return plt

def plot_wind_distributions(df):
    """Plot wind speed and direction distributions"""
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 2, 1)
    sns.histplot(df['WS'], bins=30, kde=True)
    plt.title('Wind Speed Distribution')
    
    plt.subplot(1, 2, 2)
    sns.histplot(df['WD'], bins=36, kde=True)  # 10-degree bins
    plt.title('Wind Direction Distribution')
    
    plt.tight_layout()
    return plt

def plot_ghi_histogram(df):
    """Plot GHI distribution"""
    plt.figure(figsize=(8, 5))
    sns.histplot(df['GHI'], bins=50, kde=True)
    plt.title('GHI Distribution')
    return plt