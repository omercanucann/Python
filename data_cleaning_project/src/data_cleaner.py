import pandas as pd
import numpy as np


def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def convert_types(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = ["quantity", "price_per_unit", "total_spent"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")  # "ERROR" → NaN
    return df

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    if "quantity" in df.columns:
        df["quantity"] = df["quantity"].fillna(df["quantity"].median())
    if "price_per_unit" in df.columns:
        df["price_per_unit"] = df["price_per_unit"].fillna(df["price_per_unit"].median())
    if "total_spent" in df.columns:
        df["total_spent"] = df["total_spent"].fillna(df["total_spent"].median())
    if "item" in df.columns:
        df["item"] = df["item"].fillna("Unknown")
    if "payment_method" in df.columns:
        df["payment_method"] = df["payment_method"].replace("UNKNOWN", np.nan)
        df["payment_method"] = df["payment_method"].fillna("Other")
    if "location" in df.columns:
        df["location"] = df["location"].replace("UNKNOWN", np.nan)
        df["location"] = df["location"].fillna("Unspecified")
    if "transaction_date" in df.columns:
        df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")
        df["transaction_date"] = df["transaction_date"].ffill()
    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()