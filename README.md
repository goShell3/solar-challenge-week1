# ☀️ Solar Dataset Analysis & Cross-Country Comparison

This repository provides end-to-end data profiling, cleaning, exploratory analysis, and cross-country comparison for solar datasets from Benin, Sierra Leone, and Togo.

## 📁 Repository Structure



---

## 🚀 Objectives

### Task 2: Data Profiling, Cleaning & EDA

Each country’s dataset is profiled, cleaned, and visualized with the following goals:

- **Summary Statistics**: Use `describe()` and null-value reports (`isna().sum()`) to profile data.
- **Outlier Detection**: Compute Z-scores for key columns (|Z| > 3) to flag anomalies.
- **Missing Value Handling**: Drop or impute with median values for important columns.
- **Time Series Analysis**: Plot solar irradiance and temperature metrics over time.
- **Cleaning Impact**: Analyze changes in ModA and ModB based on the `Cleaning` flag.
- **Correlation Analysis**: Generate heatmaps and scatter plots to uncover relationships.
- **Wind & Temperature Analysis**: Use wind rose, histograms, and bubble charts to visualize wind behavior and the influence of humidity on temperature and irradiance.

### Task 3: Cross-Country Comparison

- **Metric Comparison**: Side-by-side boxplots and summary tables (mean, median, std) for GHI, DNI, and DHI.
- **Statistical Testing**: ANOVA/Kruskal–Wallis to test for significant differences.
- **Ranking**: Bar chart to rank countries by average GHI.
- **Key Insights**: Highlight 3 key findings from the data.

---

## 🔑 Key Performance Indicators (KPIs)

| KPI | Description |
|-----|-------------|
| **GHI** | Global Horizontal Irradiance |
| **DNI** | Direct Normal Irradiance |
| **DHI** | Diffuse Horizontal Irradiance |
| **ModA / ModB** | Module sensor measurements |
| **TModA / TModB** | Module temperature readings |
| **Tamb** | Ambient Temperature |
| **RH** | Relative Humidity |
| **WS / WSgust** | Wind Speed & Gust Speed |
| **WD** | Wind Direction |
| **BP** | Barometric Pressure |
| **Cleaning** | Binary indicator if panel cleaning occurred |

---

## 🧠 Engineered Features

| Feature | Purpose |
|--------|---------|
| `GHI_ClearSky_Ratio` | Assess clarity of sky conditions |
| `DHI/GHI` & `DNI/GHI` | Balance of diffuse and direct radiation |
| `Hour`, `Month`, `DayOfWeek` | Time-based insights |
| `Cleaning_Delta_ModA` | Impact of cleaning on sensor output |
| `Rolling_Averages` | Smoother time series analysis |

---

## 📈 Visuals & Plots

- Line/Bar Charts: GHI, DNI, DHI, Tamb vs. Timestamp
- Correlation Heatmaps
- Scatter Plots: WS/WD/RH vs. GHI or Tamb
- Bubble Chart: GHI vs. Tamb (size = RH/BP)
- Histograms & Wind Roses
- Boxplots for cross-country GHI/DNI/DHI
- Cleaning impact visualizations

---

## 🧹 Cleaning Strategy

- Z-score outlier detection (|Z| > 3) on key numeric fields
- Null-value imputation (median for critical fields)
- Removal of erroneous or extreme outliers
- Export cleaned files to:  
  - `data/benin_clean.csv`  
  - `data/sierra_leone_clean.csv`  
  - `data/togo_clean.csv`

*Note: `/data` directory is gitignored to prevent committing large CSVs.*

---

## 📝 Requirements

- Python 3.8+
- Pandas, NumPy, Seaborn, Matplotlib, Plotly, SciPy
- Jupyter Notebook
- Windrose (for wind direction analysis)

Install with:

```bash
pip install -r requirements.txt
