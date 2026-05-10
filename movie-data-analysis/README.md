````markdown
# Movie Catalog Data Cleaning and Visualization

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

End-to-end **Python** workflow to clean, process, and visualize a **movie and streaming-content catalog dataset** (`n_movies.csv`). The project is structured for beginners, GitHub portfolios, and resume projects.

---

## Project Overview

This project demonstrates:

- Data cleaning using Pandas
- Handling missing values and duplicates
- Feature engineering
- Exploratory Data Analysis (EDA)
- Data visualization using Matplotlib and Seaborn
- Exporting cleaned datasets and figures

---

## Dataset

### Input File

```text
n_movies.csv
```

### Columns

- `title`
- `year`
- `certificate`
- `duration`
- `genre`
- `rating`
- `description`
- `stars`
- `votes`

### Derived Features

The notebook creates:

- `start_year`
- `votes_numeric`
- `duration_minutes`

---

## Repository Structure

```text
movie-data-analysis/
├── data/
│   ├── n_movies.csv
│   └── cleaned_movies.csv
├── notebooks/
│   └── analysis.ipynb
├── reports/
│   └── final_report.md
├── src/
│   └── cleaning.py
├── visuals/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Skills Demonstrated

- Data cleaning using Pandas
- Handling missing values and duplicates
- Feature engineering
- Exploratory Data Analysis (EDA)
- Data visualization using Matplotlib and Seaborn
- Python project structuring
- Jupyter Notebook workflow
- Git and GitHub project management

---

## Installation

Install required libraries:

```bash
pip install -r requirements.txt
```

### Windows PowerShell Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## How to Run

1. Open the project in VS Code
2. Select the Python interpreter
3. Open:

```text
notebooks/analysis.ipynb
```

4. Run all notebook cells

---

## Outputs

| Output | Location |
|--------|----------|
| Cleaned dataset | `data/cleaned_movies.csv` |
| Visualizations | `visuals/` folder |
| Final report | `reports/final_report.md` |

---

## Visualizations Generated

- Release year histogram
- Certificate distribution count plot
- Year vs duration scatter plot
- Correlation heatmap

---

## Libraries Used

| Library | Purpose |
|---------|---------|
| pandas | Data cleaning and analysis |
| numpy | Numerical operations |
| matplotlib | Data visualization |
| seaborn | Statistical charts |
| jupyter | Notebook execution |

---

## Example Insights

- Most content was released after 2010
- Drama and comedy were the most common genres
- Titles with higher ratings generally received more user votes
- Most movie durations ranged between 90–120 minutes

---


