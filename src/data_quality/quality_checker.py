import pandas as pd


def data_quality_report(
    df: pd.DataFrame,
    id_column: str = "idx",
) -> pd.DataFrame:
    """
    Generate a basic data-quality report for a wide omics matrix.

    Parameters
    ----------
    df:
        Omics dataframe with one identifier column and sample columns.
    id_column:
        Name of the feature identifier column.

    Returns
    -------
    pd.DataFrame
        Summary table containing key data-quality metrics.
    """
    if id_column not in df.columns:
        raise ValueError(
            f"Identifier column '{id_column}' was not found."
        )

    sample_df = df.drop(columns=[id_column]).apply(
        pd.to_numeric,
        errors="coerce",
    )

    total_missing = int(sample_df.isna().sum().sum())
    total_values = int(sample_df.size)
    valid_values = sample_df.stack()

    report = pd.DataFrame(
        {
            "Metric": [
                "Number of features",
                "Number of samples",
                "Duplicate identifiers",
                "Duplicate sample names",
                "Total missing values",
                "Missing percentage (%)",
                "Fully missing features",
                "Constant features",
                "Minimum value",
                "Maximum value",
                "Mean value",
                "Median value",
                "Standard deviation",
            ],
            "Value": [
                int(df.shape[0]),
                int(sample_df.shape[1]),
                int(df[id_column].duplicated().sum()),
                int(sample_df.columns.duplicated().sum()),
                total_missing,
                round(100 * total_missing / total_values, 3)
                if total_values
                else 0.0,
                int(sample_df.isna().all(axis=1).sum()),
                int(sample_df.nunique(axis=1, dropna=True).le(1).sum()),
                float(valid_values.min()),
                float(valid_values.max()),
                round(float(valid_values.mean()), 3),
                round(float(valid_values.median()), 3),
                round(float(valid_values.std()), 3),
            ],
        }
    )

    return report
