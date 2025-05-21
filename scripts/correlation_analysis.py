import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_heatmap(df, variables=['GHI', 'DNI', 'DHI', 'TModA', 'TModB']):
    """Plot correlation heatmap for specified variables"""
    plt.figure(figsize=(10, 8))
    corr = df[variables].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Variable Correlation Matrix')
    return plt

def plot_scatter_relationships(df):
    """Plot scatter relationships between key variables"""
    plt.figure(figsize=(18, 12))
    
    # WS, WSgust, WD vs GHI
    plt.subplot(2, 3, 1)
    sns.scatterplot(x='WS', y='GHI', data=df, alpha=0.5)
    plt.title('Wind Speed vs GHI')
    
    plt.subplot(2, 3, 2)
    sns.scatterplot(x='WSgust', y='GHI', data=df, alpha=0.5)
    plt.title('Wind Gust vs GHI')
    
    plt.subplot(2, 3, 3)
    sns.scatterplot(x='WD', y='GHI', data=df, alpha=0.5)
    plt.title('Wind Direction vs GHI')
    
    # RH relationships
    plt.subplot(2, 3, 4)
    sns.scatterplot(x='RH', y='Tamb', data=df, alpha=0.5)
    plt.title('RH vs Ambient Temp')
    
    plt.subplot(2, 3, 5)
    sns.scatterplot(x='RH', y='GHI', data=df, alpha=0.5)
    plt.title('RH vs GHI')
    
    plt.tight_layout()
    return plt