import matplotlib.pyplot as plt
import seaborn as sns

class SolarVisualizer:
    def __init__(self, data):
        self.data = data


    @staticmethod  
    def plot_time_series(data, x_col, y_col, title="Time Series Plot", xlabel="Date", ylabel="Value"):
        """
        Plots a time series graph for the given data.

        Args:
            data (pd.DataFrame): DataFrame containing the data to plot.
            x_col (str): Column name for the x-axis (time).
            y_col (str): Column name for the y-axis (value).
            title (str): Title of the plot.
            xlabel (str): Label for the x-axis.
            ylabel (str): Label for the y-axis.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(data[x_col], data[y_col], marker='o', linestyle='-')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()
        plt.show()
        
    @staticmethod
    def plot_correlation_matrix(data, title="Correlation Matrix", cmap='coolwarm'):
        """
        Plots a heatmap of the correlation matrix for the given data.

        Args:
            data (pd.DataFrame): DataFrame containing the data to plot.
            title (str): Title of the plot.
            cmap (str): Colormap for the heatmap.
        """
        plt.figure(figsize=(12, 8))
        corr = data.corr()
        sns.heatmap(corr, annot=True, fmt=".2f", cmap=cmap)
        plt.title(title)
        plt.show()