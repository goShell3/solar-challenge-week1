import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_cleaning_impact(df, module_cols=['ModA', 'ModB']):
    """Plot module performance pre/post cleaning"""
    if 'Cleaning_Flag' not in df.columns:
        raise ValueError("DataFrame must contain 'Cleaning_Flag' column")
    
    plt.figure(figsize=(15, 6))
    for i, mod in enumerate(module_cols, 1):
        plt.subplot(1, len(module_cols), i)
        sns.barplot(x='Cleaning_Flag', y=mod, data=df, ci='sd')
        plt.title(f'{mod} Performance by Cleaning Status')
        plt.ylabel('Performance')
    plt.tight_layout()
    return plt

def plot_cleaning_timeseries(df, module_cols=['ModA', 'ModB']):
    """Plot module performance around cleaning events"""
    cleaning_dates = df[df['Cleaning_Flag'] == 1].index
    
    plt.figure(figsize=(15, 8))
    for mod in module_cols:
        plt.plot(df.index, df[mod], label=mod, alpha=0.7)
    
    for date in cleaning_dates:
        plt.axvline(date, color='red', linestyle='--', alpha=0.5)
    
    plt.title('Module Performance with Cleaning Events')
    plt.ylabel('Performance')
    plt.legend()
    plt.grid(True)
    return plt