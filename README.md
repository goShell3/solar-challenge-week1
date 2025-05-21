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

