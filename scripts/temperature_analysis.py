import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_rh_temperature_relationship(df):
    """Plot RH vs temperature relationships"""
    plt.figure(figsize=(15, 6))
    
    plt.subplot(1, 2, 1)
    sns.scatterplot(x='RH', y='Tamb', hue='GHI', data=df, palette='viridis')
    plt.title('RH vs Ambient Temp colored by GHI')
    
    plt.subplot(1, 2, 2)
    sns.scatterplot(x='RH', y='TModA', hue='GHI', data=df, palette='viridis')
    plt.title('RH vs Module Temp colored by GHI')
    
    plt.tight_layout()
    return plt

def plot_bubble_chart(df):
    """Plot GHI vs Tamb with bubble size based on RH"""
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(
        x='Tamb', 
        y='GHI', 
        s=df['RH']*2,  # Scale RH for bubble size
        c=df['BP'],     # Color by barometric pressure
        alpha=0.6,
        data=df,
        cmap='viridis'
    )
    plt.colorbar(scatter, label='Barometric Pressure')
    plt.xlabel('Ambient Temperature (°C)')
    plt.ylabel('GHI (W/m²)')
    plt.title('GHI vs Temperature (Bubble Size = RH)')
    plt.grid(True)
    return plt