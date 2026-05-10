# Data-Cleaning-Project

End-to-end **Python** workflow to clean and visualize a **Netflix / IMDb-style title catalog** (`n_movies.csv`). The project is structured for **beginners**, **GitHub**, and **resume** use: clear folders, commented `src` helpers, a step-by-step notebook, saved figures, and a written report template.

---

## What you analyze

| Item | Detail |
|------|--------|
| **Your file** | `%USERPROFILE%\Downloads\netfilx\n_movies.csv` (loaded **first** when it exists) |
| **Project copies** | `data/n_movies.csv` and/or `data/netfilx/n_movies.csv` (optional) |
| **Fallback** | `data/raw_data.csv` (tiny demo if no `n_movies.csv` is found anywhere above) |

**Columns in `n_movies.csv`:** `title`, `year`, `certificate`, `duration`, `genre`, `rating`, `description`, `stars`, `votes`.

The notebook derives **`start_year`** (from the `year` string), **`votes_numeric`** (comma-free counts), and **`duration_minutes`** for analysis and charts.

---

## Repository layout

```text
Data-Cleaning-Project/
├── data/
│   ├── n_movies.csv           # Optional local copy of your catalog
│   ├── netfilx/
│   │   └── n_movies.csv       # Optional nested copy (same schema)
│   ├── raw_data.csv           # Fallback teaching dataset
│   ├── cleaned_n_movies.csv   # Written when you run the notebook (n_movies mode)
│   └── cleaned_netflix.csv    # Written in raw_data demo mode
├── notebooks/
│   └── analysis.ipynb         # Main entry: load → clean → visualize
├── visuals/                   # PNG exports (histogram, count, scatter, heatmap)
├── reports/
│   └── final_report.md        # Fill in after running the notebook
├── src/
│   └── cleaning.py            # Reusable cleaning functions
├── requirements.txt
└── README.md
```

**Important:** The notebook **reads** your Downloads file but **does not** modify it. All cleaned data and images are written under **`data/`** and **`visuals/`** in this project.

---

## Installation

```bash
pip install -r requirements.txt
```

**Windows (PowerShell), from this folder:**

```powershell
cd Data-Cleaning-Project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## How to run

1. Open **`Data-Cleaning-Project`** in **VS Code** or **Cursor**.
2. Choose the Python interpreter where you installed the requirements (your `.venv` if you created one).
3. Open **`notebooks/analysis.ipynb`** and run **Run All** (or start Jupyter: `jupyter notebook notebooks/analysis.ipynb`).

### Path priority (same as the notebook)

1. **`DATA_PATH_OVERRIDE`** in the first code cell (if you set a `Path`)
2. **`Downloads\netfilx\n_movies.csv`**
3. **`data/n_movies.csv`**
4. **`data/netfilx/n_movies.csv`**
5. **`data/raw_data.csv`** (if nothing else is present, the notebook raises a clear error listing expected locations)

If your CSV lives elsewhere, set in the notebook:

```python
DATA_PATH_OVERRIDE = Path(r"C:\path\to\n_movies.csv")
```

### Outputs after a successful run

| Output | Location |
|--------|----------|
| Cleaned table | `data/cleaned_n_movies.csv` |
| Figures | `visuals/histogram_release_year.png`, `countplot_content_type.png`, `scatter_year_vs_duration.png`, `correlation_heatmap.png` |
| Numbers for prose | Section **“Summary for final_report.md”** in the notebook |

---

## Libraries

| Package | Role |
|---------|------|
| **pandas** | Tables, I/O, cleaning |
| **numpy** | Numeric helpers |
| **matplotlib** | Plotting backend |
| **seaborn** | Statistical charts and heatmaps |
| **jupyter** / **ipykernel** | Notebook runtime |

---

## Using `cleaning.py` outside the notebook

```python
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent  # or your project root
sys.path.insert(0, str(ROOT / "src"))
import cleaning as cl
```

---

## License & data notice

Educational and portfolio use. **`n_movies.csv`** is user-supplied or third-party catalog-style data; it is **not** an official Netflix data product. Replace bracketed sections in **`reports/final_report.md`** with your own wording before publishing.
