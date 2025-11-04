# Seaborn Data Visualization Tutorial

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Latest-green.svg)](https://seaborn.pydata.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/sekertutku/Machine-Learning---Regression-Models)

## Overview

This repository provides a comprehensive tutorial on data visualization using the Seaborn library in Python. The project demonstrates 12 distinct visualization techniques through practical examples using real-world datasets related to socioeconomic indicators and police incidents in the United States, showcasing Seaborn's powerful statistical plotting capabilities.

## 🎮 Interactive Demo

**👉 [Run the Interactive Notebook on Kaggle](https://www.kaggle.com/code/dandrandandran2093/seaborn-first-steps)**

*For the best experience with pre-configured datasets and instant execution, use the Kaggle notebook above. All visualizations are ready to run!*

## Table of Contents

- [Introduction](#introduction)
- [Datasets](#datasets)
- [Visualization Types](#visualization-types)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Key Insights](#key-insights)
- [Contributing](#contributing)
- [References](#references)

## Introduction

Seaborn is a Python data visualization library based on matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics. This tutorial covers fundamental to advanced visualization techniques, demonstrating how to effectively communicate data insights through various plot types.

## Datasets

The analysis utilizes five primary datasets:

1. **MedianHouseholdIncome2015**: Median household income statistics by geographic area
2. **PercentagePeopleBelowPovertyLevel**: Proportion of population below the poverty threshold
3. **PercentOver25CompletedHighSchool**: High school graduation rates for individuals aged 25 and above
4. **ShareRaceByCity**: Demographic distribution of racial groups across cities
5. **PoliceKillingsUS**: Records of police-involved fatalities with demographic and situational metadata

## Visualization Types

The tutorial demonstrates 12 distinct visualization techniques:

### 1. Bar Plot
- Comparative analysis of poverty rates across states
- Frequency distribution of names in police killings dataset
- High school graduation rates by geographic area
- Racial demographic composition by state

**Use Cases:**
- Categorical comparisons
- Aggregated statistics
- Ranked data visualization

### 2. Point Plot
- Correlation analysis between poverty rates and high school graduation
- Normalized trend visualization across geographic areas

**Use Cases:**
- Showing trends over categories
- Comparing group means
- Highlighting changes

### 3. Joint Plot
- Bivariate distribution analysis using kernel density estimation
- Scatter plot with marginal distributions

**Use Cases:**
- Exploring relationships between two variables
- Understanding distributions simultaneously
- Detecting patterns and outliers

### 4. Pie Chart
- Racial composition in police killings dataset
- Proportional representation with percentage annotations

**Use Cases:**
- Showing proportions
- Part-to-whole relationships
- Demographic breakdowns

### 5. Linear Model Plot (lmplot)
- Regression analysis of poverty vs. education metrics
- Statistical relationship visualization with confidence intervals

**Use Cases:**
- Regression analysis
- Correlation visualization
- Trend prediction

### 6. KDE Plot (Kernel Density Estimation)
- Continuous probability density visualization
- Multivariate distribution analysis

**Use Cases:**
- Smooth distribution curves
- Probability density estimation
- Comparing distributions

### 7. Violin Plot
- Distribution comparison with embedded box plots
- Density estimation across categories

**Use Cases:**
- Comparing distributions across categories
- Showing full distribution shape
- Detecting multimodal distributions

### 8. Heatmap
- Correlation matrix visualization
- Annotated numerical relationships between variables

**Use Cases:**
- Correlation analysis
- Matrix data visualization
- Pattern detection in tabular data

### 9. Box Plot
- Distribution analysis of age by gender and manner of death
- Outlier detection and quartile visualization

**Use Cases:**
- Statistical summaries
- Outlier detection
- Comparing distributions

### 10. Swarm Plot
- Categorical scatter plot showing individual data points
- Distribution patterns across discrete categories

**Use Cases:**
- Showing all data points
- Small to medium datasets
- Avoiding overplotting

### 11. Pair Plot
- Pairwise relationship exploration
- Comprehensive multivariate analysis

**Use Cases:**
- Exploratory data analysis
- Understanding multiple relationships
- Feature selection

### 12. Count Plot
- Frequency distribution of categorical variables
- Analysis of weapon types, threat levels, and demographic factors

**Use Cases:**
- Categorical frequency analysis
- Simple bar charts with counts
- Quick data overview

## Requirements

```
python>=3.x
numpy>=1.21.0
pandas>=1.3.0
seaborn>=0.11.0
matplotlib>=3.4.0
jupyter>=1.0.0
```

## Installation

### Option 1: Use Kaggle (Recommended) ⭐

The easiest way to explore this tutorial is on Kaggle where everything is pre-configured:

👉 **[Open Interactive Notebook on Kaggle](https://www.kaggle.com/code/dandrandandran2093/seaborn-first-steps)**

### Option 2: Run Locally

1. Clone the repository:
```bash
git clone https://github.com/sekertutku/SeaBorn-First-Steps.git
cd SeaBorn-First-Steps
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. **Datasets:**
   
   ✨ All datasets are included in the `input/` directory for reference:
   ```
   input/
   ├── MedianHouseholdIncome2015.csv
   ├── PercentOver25CompletedHighSchool.csv
   ├── PercentagePeopleBelowPovertyLevel.csv
   ├── PoliceKillingsUS.csv
   └── ShareRaceByCity.csv
   ```
   
   **Note:** The code uses Kaggle-specific paths (`/kaggle/input/...`). To run locally, update the dataset paths in the code from:
   ```python
   df = pd.read_csv(r"/kaggle/input/dataset-name/file.csv")
   ```
   to:
   ```python
   df = pd.read_csv("input/file.csv")
   ```

## Usage

### On Kaggle (Recommended) ⭐

Simply open the [Kaggle notebook](https://www.kaggle.com/code/dandrandandran2093/seaborn-first-steps) and run the cells. All dependencies and datasets are pre-configured!

### Locally

Execute the main script to generate all visualizations:

```bash
python seaborn-first-steps.py
```

Or run individual sections in a Jupyter notebook environment:

```bash
jupyter notebook seaborn-first-steps.ipynb
```

### Example Code

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("input/MedianHouseholdIncome2015.csv")

# Create bar plot
sns.barplot(x='State', y='Income', data=df)
plt.xticks(rotation=90)
plt.show()

# Create correlation heatmap
correlation = df.corr()
sns.heatmap(correlation, annot=True, fmt=".2f")
plt.show()
```

## Key Insights

The analysis reveals several important findings:

### Socioeconomic Patterns
- **Strong Negative Correlation**: Poverty rates and high school graduation rates show an inverse relationship across states (r ≈ -0.7)
- **Income Inequality**: Significant variation in median household income across geographic areas
- **Education Impact**: States with higher graduation rates consistently show lower poverty levels

### Demographic Analysis
- **Geographic Diversity**: Racial composition varies dramatically across different cities and states
- **Regional Patterns**: Certain areas exhibit distinct demographic profiles

### Statistical Findings
- **Distribution Shapes**: Most socioeconomic metrics show normal or slightly skewed distributions
- **Outlier Detection**: Box plots reveal interesting outliers in income and education data
- **Multivariate Relationships**: Pair plots demonstrate complex interactions between multiple variables

### Visualization Effectiveness
- **Heatmaps** excel at showing correlation patterns
- **Violin plots** effectively display distribution shapes across categories
- **Joint plots** reveal bivariate relationships with marginal distributions
- **Swarm plots** work well for smaller datasets with categorical groupings

## Key Features

### Statistical Visualizations
- **Built-in Statistics**: Automatic calculation of means, medians, and confidence intervals
- **Distribution Fitting**: KDE and histogram overlays
- **Regression Lines**: Linear model fitting with confidence bands

### Aesthetic Control
- **Color Palettes**: Multiple built-in color schemes
- **Themes**: Professional styling options
- **Customization**: Fine-grained control over plot elements

### Integration
- **Pandas Compatibility**: Direct dataframe support
- **Matplotlib Foundation**: Full access to matplotlib features
- **Statistical Focus**: Designed for statistical analysis

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss proposed modifications.

### How to Contribute
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## References

### Course
- **Udemy**: Data Science by DATAI TEAM

### Tutorial
- Kaggle Notebook: [Seaborn Tutorial for Beginners](https://www.kaggle.com/code/kanncaa1/seaborn-tutorial-for-beginners)

### Documentation
- [Seaborn Official Documentation](https://seaborn.pydata.org/)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Seaborn API Reference](https://seaborn.pydata.org/api.html)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)

### Related Project
- 📊 [Plotly Data Visualization Tutorial](https://github.com/sekertutku/Plotly-First-Steps) | [Kaggle](https://www.kaggle.com/code/dandrandandran2093/plotly-first-steps)

## Acknowledgments

Special thanks to:
- DATAI TEAM for the comprehensive data science course
- The Seaborn development team for creating an excellent visualization library
- Data providers for making these datasets available for educational purposes
- The open-source community for continuous support and contributions

---

**Note**: This tutorial is intended for educational purposes. The datasets contain sensitive information and should be analyzed with appropriate ethical considerations.

## 📞 Connect

If you have questions or suggestions:
- Open an issue in this repository
- Connect on [Kaggle](https://www.kaggle.com/dandrandandran2093)
- Visit my website: [tutkufurkan.com](https://www.tutkufurkan.com/)
- Star this repository if you found it helpful!

---

**Happy Visualizing! 📊✨**

🌐 More projects at [tutkufurkan.com](https://www.tutkufurkan.com/)
