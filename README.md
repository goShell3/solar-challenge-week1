# Solar Potential Analysis Project

## 🌍 Cross-Country Solar Potential Comparison

This project analyzes and compares solar irradiation data across Benin, Sierra Leone, and Togo to identify relative solar potential and key differences between these West African nations.

## 📂 Project Structure

```
solar-analysis/
├── data/
│   ├── raw/                  # Original data files
│   ├── processed/            # Cleaned country datasets
│   └── outputs/              # Analysis results
├── notebooks/
│   ├── 1_data_cleaning.ipynb
│   ├── 2_country_analysis.ipynb
│   └── 3_comparison.ipynb    # Main comparison notebook
├── src/
│   ├── data_cleaner.py       # Data preprocessing
│   ├── feature_engineer.py   # Feature generation
│   └── visualization.py      # Plotting functions
└── README.md
```

## 🔄 Workflow Pipeline

1. **Data Preparation**
   - Load raw CSV files for each country
   - Standardize timestamps and column names
   - Handle missing values and outliers

2. **Country-Specific Cleaning**
   ```python
   # Sample cleaning pipeline per country
   cleaner = (
       SolarDataCleaner(df)
       .add_time_features()
       .handle_missing_values()
       .remove_outliers()
       .validate_ranges()
   )
   cleaned_df = cleaner.get_clean_data()
   ```

3. **Comparative Analysis**
   - Generate side-by-side visualizations
   - Calculate summary statistics
   - Perform statistical significance testing

4. **Key Metric Comparison**
   - Global Horizontal Irradiance (GHI)
   - Direct Normal Irradiance (DNI)
   - Diffuse Horizontal Irradiance (DHI)

## 📊 Analysis Steps

### 1. Data Loading & Preparation
- Load each country's cleaned dataset
- Ensure consistent datetime indexing
- Verify all metrics exist in each dataset

### 2. Visual Comparison
```python
# Generate comparison boxplots
plot_comparison_boxplots(
    metrics=['GHI', 'DNI', 'DHI'],
    countries=['benin', 'sierra_leone', 'togo'],
    data=cleaned_data
)
```

### 3. Statistical Analysis
- **ANOVA Testing**: 
  ```python
  stats.f_oneway(benin_ghi, sierraleone_ghi, togo_ghi)
  ```
- **Post-hoc Tests** (if ANOVA significant):
  ```python
  stats.tukey_hsd(benin_ghi, sierraleone_ghi, togo_ghi)
  ```

### 4. Key Findings Documentation
- Create markdown summary of:
  - Highest potential countries
  - Variability observations
  - Atmospheric condition inferences

## 💡 Interpretation Guide

| Metric | Ideal Characteristics | Significance |
|--------|-----------------------|--------------|
| GHI    | Higher values         | Overall solar potential |
| DNI    | High + Stable         | Good for concentrated solar |
| DHI    | Low relative to GHI   | Clear atmosphere |

## 🚀 Running the Analysis

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute notebooks in order:
   ```
   1_data_cleaning.ipynb → 2_country_analysis.ipynb → 3_comparison.ipynb
   ```

3. View outputs in:
   - `data/outputs/` for numerical results
   - `notebooks/figures/` for visualizations

## 📝 Key Observations Template

```markdown
### Comparative Insights

1. **Highest Potential**: [Country] shows the highest median GHI at [X] W/m²
2. **Consistency**: [Country] demonstrates the most stable radiation (IQR = [X])
3. **Atmospheric**: [Country]'s low DHI/DNI ratio suggests [characteristic]
```

## 🔍 Further Analysis Suggestions

- Seasonal variation decomposition
- Cloud cover impact analysis
- Solar farm yield simulations
- Economic feasibility projections

This systematic approach enables scientifically rigorous comparison of solar potential across West African nations, supporting data-driven energy policy decisions.