import matplotlib.pyplot as plt
import seaborn as sns
from windrose import WindroseAxes
import plotly.express as px

class SolarDataVisualizer:
    
    def __init__(self, df):
        self.df = df

    # @staticmethod
    def plot_time_series(self):
        self.df.set_index("Timestamp")[["GHI", "DNI", "DHI", "Tamb"]].plot(figsize=(15, 6))
        plt.title("Solar Irradiance and Temperature over Time")
        plt.show()
        
    def plot_hourly_avg(self):
        self.df['Hour'] = self.df['Timestamp'].dt.hour
        self.df.groupby('Hour')[['GHI', 'DNI', 'DHI', 'Tamb']].mean().plot()
        plt.title("Average Values by Hour")
        plt.show()

    def cleaning_impact(self):
        self.df.groupby("Cleaning")[["ModA", "ModB"]].mean().plot(kind="bar")
        plt.title("Effect of Cleaning on ModA and ModB")
        plt.ylabel("W/m²")
        plt.show()

    def plot_correlation(self):
        sns.heatmap(self.df[["GHI", "DNI", "DHI", "TModA", "TModB"]].corr(), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.show()

    def scatter_relationships(self):
        sns.scatterplot(x="WS", y="GHI", data=self.df)
        plt.title("WS vs GHI")
        plt.show()

    def wind_rose(self):
        ax = WindroseAxes.from_ax()
        ax.bar(self.df["WD"], self.df["WS"], normed=True, opening=0.8, edgecolor='white')
        ax.set_legend()
        plt.title("Wind Rose")
        plt.show()

    def bubble_chart(self):
        fig = px.scatter(self.df, x="Tamb", y="GHI", size="RH", color="BP", 
                        title="GHI vs Tamb with RH(Bubble) and BP(Color)")
        fig.show()