<<<<<<< HEAD
# Solar Energy Solutions

## 🔑 Major KPIs (Key Performance Indicators)

These are the **core metrics** that measure solar potential, environmental influence, and system performance:

| KPI                                     | Description                                             | Why It’s Important                                           |
| --------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| **GHI** (Global Horizontal Irradiance)  | Total solar radiation received per m²                   | Primary indicator of total solar energy potential            |
| **DNI** (Direct Normal Irradiance)      | Direct sunlight on a surface perpendicular to sun rays  | Critical for solar panel orientation and tracking systems    |
| **DHI** (Diffuse Horizontal Irradiance) | Scattered sunlight (non-direct) on a horizontal surface | Useful in cloudy conditions; impacts total energy collected  |
| **ModA / ModB**                         | Sensor measurements of solar modules                    | Proxy for energy output and panel performance                |
| **Tamb** (Ambient Temperature)          | Air temperature near the solar site                     | Affects solar panel efficiency and degradation               |
| **TModA / TModB**                       | Module temperatures                                     | Key for evaluating thermal behavior and efficiency           |
| **WS / WSgust**                         | Wind speed & gusts                                      | Influences cooling of panels; affects panel structure/design |
| **WD** (Wind Direction)                 | Direction of wind flow                                  | For design of solar arrays and predicting dust accumulation  |
| **RH** (Relative Humidity)              | Moisture content in the air                             | High RH may reduce irradiance, cause soiling or condensation |
| **BP** (Barometric Pressure)            | Atmospheric pressure                                    | Indirect environmental factor; useful in weather modeling    |
| **Cleaning Flag**                       | Indicates if cleaning was done                          | Used to evaluate the impact of cleaning on performance       |

---

## 📊 Key Features You’re Working With or Should Add

Here’s a categorization of **existing + recommended engineered features**:

### 🌞 Solar & Energy Features

* `GHI`, `DNI`, `DHI`
* `ModA`, `ModB`
* `TModA`, `TModB`
* **Recommended**: `Clearsky Index`, `DNI/GHI`, `DHI/GHI` ratios

### 🌦️ Weather & Environmental Features

* `Tamb`, `RH`, `BP`, `Precipitation`
* `WS`, `WSgust`, `WD`
* **Recommended**: Wind Rose vectors, RH influence on Tamb/GHI

### 🧹 Cleaning & Maintenance Features

* `Cleaning` flag (binary)
* **Recommended**: `ModA_before_clean`, `ModA_after_clean` averages

### 🕒 Time-based Features

* `Timestamp`
* **Recommended**: `Hour`, `Day`, `Month`, `Season`, `DayOfWeek`

### 🔍 Analytical/Derived Features

* Z-scores for outlier detection on all KPIs
* **Recommended**: Rolling averages for smoother trend analysis
* **Recommended**: Delta/change features (e.g. `ModA.diff()`)

---

## 🎯 Feature-KPI Alignment with Tasks

| Task Element                            | Relevant KPIs/Features                                 |
| --------------------------------------- | ------------------------------------------------------ |
| **Summary Statistics & Missing Report** | All numeric features (`describe()`, `isna()`)          |
| **Outlier Detection**                   | GHI, DNI, DHI, ModA, ModB, WS, WSgust (Z-scores)       |
| **Cleaning Impact**                     | Cleaning flag + ModA/ModB before/after analysis        |
| **Time Series Trends**                  | GHI, DNI, DHI, Tamb vs Timestamp (add `Month`, `Hour`) |
| **Correlation Heatmap**                 | GHI, DNI, DHI, TModA, TModB, RH, Tamb                  |
| **Scatter Relationships**               | WS, WD, RH vs GHI/Tamb                                 |
| **Wind Analysis**                       | WS, WSgust, WD (visualized with Wind Rose)             |
| **Temperature Analysis**                | RH vs Tamb, RH vs GHI                                  |
| **Bubble Plot**                         | GHI (x), Tamb (y), RH/BP as bubble size                |
| **Cross-Country Comparison**            | Mean/median/stdev of GHI, DNI, DHI across countries    |

---

## ✅ Suggested Additional Features

| Feature                                     | Purpose                                       |
| ------------------------------------------- | --------------------------------------------- |
| `GHI_ClearSky_Ratio`                        | Assess sky clarity and solar efficiency       |
| `Daylight_Hours` (using solar position lib) | Normalize irradiance and production potential |
| `GHI_per_Hour`                              | Normalize energy potential over time          |
| `Cleaning_Delta_ModA`                       | Difference before/after cleaning              |

=======
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
>>>>>>> 87b8250acc9dc029fc4434812d6628c00040c918
