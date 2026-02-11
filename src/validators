def validate_required_columns(df, required):
    errors = []

    for col in required:
        if col not in df.columns:
            errors.append(f"Missing column: {col}")
        elif df[col].isna().sum() > 0:
            errors.append(f"{col} has missing values")

    return errors


def find_duplicates(df, subset):
    if not all(c in df.columns for c in subset):
        return []

    dup = df[df.duplicated(subset=subset, keep=False)]

    return [f"{k}: {len(v)} rows" for k, v in dup.groupby(subset)]
