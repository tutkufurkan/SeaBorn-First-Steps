# Seaborn Data Visualization Tutorial

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Latest-green.svg)](https://seaborn.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository provides a comprehensive tutorial on data visualization using the Seaborn library in Python. The project demonstrates various visualization techniques through practical examples using real-world datasets related to socioeconomic indicators and police incidents in the United States.

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

### 2. Point Plot
- Correlation analysis between poverty rates and high school graduation
- Normalized trend visualization across geographic areas

### 3. Joint Plot
- Bivariate distribution analysis using kernel density estimation
- Scatter plot with marginal distributions

### 4. Pie Chart
- Racial composition in police killings dataset
- Proportional representation with percentage annotations

### 5. Linear Model Plot (lmplot)
- Regression analysis of poverty vs. education metrics
- Statistical relationship visualization with confidence intervals

### 6. KDE Plot (Kernel Density Estimation)
- Continuous probability density visualization
- Multivariate distribution analysis

### 7. Violin Plot
- Distribution comparison with embedded box plots
- Density estimation across categories

### 8. Heatmap
- Correlation matrix visualization
- Annotated numerical relationships between variables

### 9. Box Plot
- Distribution analysis of age by gender and manner of death
- Outlier detection and quartile visualization

### 10. Swarm Plot
- Categorical scatter plot showing individual data points
- Distribution patterns across discrete categories

### 11. Pair Plot
- Pairwise relationship exploration
- Comprehensive multivariate analysis

### 12. Count Plot
- Frequency distribution of categorical variables
- Analysis of weapon types, threat levels, and demographic factors

## Requirements

```
python >= 3.x
numpy
pandas
seaborn
matplotlib
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/seaborn-tutorial.git
cd seaborn-tutorial
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Download the datasets and place them in the `input/` directory.

## Usage

Execute the main script to generate all visualizations:

```bash
python seaborn-first-steps.py
```

Or run individual sections in a Jupyter notebook environment:

```bash
jupyter notebook notebook.ipynb
```

## Key Insights

The analysis reveals several important findings:

- **Socioeconomic Correlation**: Strong negative correlation between poverty rates and high school graduation rates across states
- **Demographic Patterns**: Significant variation in racial composition across different geographic areas
- **Police Incidents**: Notable demographic disparities in police-involved fatalities
- **Geographic Trends**: Certain states exhibit consistently higher rates across multiple socioeconomic indicators

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss proposed modifications.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## References

- Udemy Course: Data Science by DATAI TEAM
- Kaggle Notebook: [Seaborn Tutorial for Beginners](https://www.kaggle.com/code/kanncaa1/seaborn-tutorial-for-beginners)
- [Seaborn Official Documentation](https://seaborn.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)

## Acknowledgments

Special thanks to the data providers and the open-source community for making these datasets available for educational purposes.

---

**Note**: This tutorial is intended for educational purposes. The datasets contain sensitive information and should be analyzed with appropriate ethical considerations.
