import re
import pandas as pd


def normalize_columns(df):
    df = df.copy()

    def clean(c):
        c = c.strip().lower()
        c = re.sub(r"[^\w\s]", "", c)
        return c.replace(" ", "_")

    df.columns = [clean(c) for c in df.columns]
    return df


def basic_cleaning(df):
    df = df.copy()

    df = df.dropna(how="all")

    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.strip()

    return df
