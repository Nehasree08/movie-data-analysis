"""
Reusable data cleaning helpers for tabular movie/TV catalog data.

Works with the small teaching CSV (`raw_data.csv`) and with `n_movies.csv`
(IMDb-style: title, year, certificate, duration, genre, rating, votes, …).
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(path)


def parse_imdb_style_start_year(series: pd.Series) -> pd.Series:
    """
    Pull the first 4-digit year from strings like '(2018– )' or '(2016–2022)'.

    Returns floats (e.g. 2018.0) so the column can be used in describe/plots.
    """
    extracted = series.astype(str).str.extract(r"\((\d{4})", expand=False)
    return pd.to_numeric(extracted, errors="coerce")


def clean_vote_counts(series: pd.Series) -> pd.Series:
    """Turn vote strings such as '177,031' into integers (errors → NaN)."""
    s = series.astype(str).str.replace(",", "", regex=False).str.strip()
    return pd.to_numeric(s, errors="coerce")


def parse_duration_minutes(series: pd.Series) -> pd.Series:
    """Parse values like '30 min' / '178 min' into numeric minutes."""
    extracted = series.astype(str).str.extract(r"(?i)(\d+)\s*min", expand=False)
    return pd.to_numeric(extracted, errors="coerce")


def enrich_n_movies_schema(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add standard numeric columns for the `n_movies.csv` layout.

    Expects columns: year, votes, duration (and keeps all original columns).
    """
    out = df.copy()
    out["start_year"] = parse_imdb_style_start_year(out["year"])
    out["votes_numeric"] = clean_vote_counts(out["votes"])
    out["duration_minutes"] = parse_duration_minutes(out["duration"])
    return out


def dataset_info(df: pd.DataFrame) -> None:
    """Print shape, dtypes, missing counts, and memory usage (beginner-friendly overview)."""
    print("=== Shape (rows, columns) ===")
    print(df.shape)
    print("\n=== Column types ===")
    print(df.dtypes)
    print("\n=== Missing values per column ===")
    print(df.isna().sum())
    print("\n=== First rows ===")
    print(df.head())
    print("\n=== describe() for numeric columns ===")
    print(df.describe(include=[np.number]))


def handle_missing_values(
    df: pd.DataFrame,
    *,
    fill_text: str = "Unknown",
    numeric_fill: float | None = None,
) -> pd.DataFrame:
    """
    Fill missing values in a sensible default way for this project.

    - Object (text) columns: fill with fill_text
    - Numeric columns: fill with median if numeric_fill is None, else numeric_fill
    """
    out = df.copy()

    for col in out.select_dtypes(include=["object"]).columns:
        out[col] = out[col].fillna(fill_text)

    num_cols = out.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        if out[col].isna().any():
            fill_val = (
                out[col].median()
                if numeric_fill is None
                else numeric_fill
            )
            out[col] = out[col].fillna(fill_val)

    return out


def remove_duplicates(df: pd.DataFrame, subset: list[str] | None = None) -> pd.DataFrame:
    """Drop duplicate rows. If subset is given, only those columns define a duplicate."""
    return df.drop_duplicates(subset=subset, keep="first").reset_index(drop=True)


def remove_outliers_iqr(
    df: pd.DataFrame,
    column: str,
    factor: float = 1.5,
) -> pd.DataFrame:
    """
    Remove rows where `column` is outside the IQR fence.

    Q1 - factor*IQR ... Q3 + factor*IQR is kept; extreme rows are dropped.
    Good for numeric columns like release_year when you have bad data years.
    """
    out = df.copy()
    if column not in out.columns:
        raise KeyError(f"Column not found: {column}")

    series = out[column]
    if not pd.api.types.is_numeric_dtype(series):
        raise TypeError(f"Column {column} must be numeric for IQR outlier removal.")

    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    low = q1 - factor * iqr
    high = q3 + factor * iqr
    mask = (series >= low) & (series <= high)
    return out.loc[mask].reset_index(drop=True)


def save_cleaned_csv(df: pd.DataFrame, path: str | Path) -> None:
    """Save cleaned DataFrame to CSV (creates parent folders if needed)."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
