import pandas as pd


def convert_to_numeric(
    df: pd.DataFrame,
    id_column: str = "idx",
) -> pd.DataFrame: 
    """
    Convert all sample columns to numeric values.
    """

    df = df.copy()

    sample_columns = [col for col in df.columns if col != id_column]

    df[sample_columns] = df[sample_columns].apply(
        pd.to_numeric,
        errors="coerce",
    )

    return df

def missingness_report(
    df: pd.DataFrame,
    id_column: str = "idx",
) -> pd.DataFrame:
    """
    Calculate missing-value counts and percentages for each feature.

    Parameters
    ----------
    df:
        Wide omics dataframe with features in rows and samples in columns.
    id_column:
        Name of the feature identifier column.

    Returns
    -------
    pd.DataFrame
        Feature-level missingness report.
    """
    if id_column not in df.columns:
        raise ValueError(f"Identifier column '{id_column}' was not found.")

    sample_columns = [col for col in df.columns if col != id_column]
    numeric_df = df[sample_columns].apply(pd.to_numeric, errors="coerce")

    report = pd.DataFrame(
        {
            id_column: df[id_column],
            "missing_count": numeric_df.isna().sum(axis=1),
            "missing_percentage": numeric_df.isna().mean(axis=1) * 100,
        }
    )

    return report.sort_values(
        "missing_percentage",
        ascending=False,
    ).reset_index(drop=True)


import pandas as pd


import pandas as pd


def remove_sparse_features(
    df: pd.DataFrame,
    id_column: str = "idx",
    max_missing_percentage: float = 30.0,
) -> pd.DataFrame:
    """
    Remove features whose missing-value percentage exceeds a threshold.

    Parameters
    ----------
    df:
        Wide omics dataframe with features in rows and samples in columns.
    id_column:
        Name of the feature identifier column.
    max_missing_percentage:
        Maximum allowed missingness percentage for a feature.

    Returns
    -------
    pd.DataFrame
        Filtered dataframe.
    """
    if id_column not in df.columns:
        raise ValueError(
            f"Identifier column '{id_column}' was not found."
        )

    if not 0 <= max_missing_percentage <= 100:
        raise ValueError(
            "max_missing_percentage must be between 0 and 100."
        )

    sample_columns = [
        column for column in df.columns
        if column != id_column
    ]

    numeric_data = df[sample_columns].apply(
        pd.to_numeric,
        errors="coerce",
    )

    missing_percentage = numeric_data.isna().mean(axis=1) * 100

    keep_mask = missing_percentage <= max_missing_percentage

    return df.loc[keep_mask].reset_index(drop=True)



def remove_constant_features(
    df: pd.DataFrame,
    id_column: str = "idx",
) -> pd.DataFrame:
    """
    Remove features with no variation across samples.
    """

    sample_columns = [col for col in df.columns if col != id_column]

    mask = (
        df[sample_columns]
        .nunique(axis=1, dropna=True)
        .gt(1)
    )

    return df.loc[mask].reset_index(drop=True)




def missingness_abundance_correlation(
    df: pd.DataFrame,
    id_column: str = "idx",
) -> float:
    """
    Calculate the Spearman correlation between feature abundance
    and feature-level missingness.

    Features are rows and samples are columns.

    Returns
    -------
    float
        Spearman correlation between mean feature abundance
        and missing percentage.
    """
    if id_column not in df.columns:
        raise ValueError(
            f"Identifier column '{id_column}' was not found."
        )

    sample_columns = [
        column for column in df.columns
        if column != id_column
    ]

    numeric_data = df[sample_columns].apply(
        pd.to_numeric,
        errors="coerce",
    )

    mean_abundance = numeric_data.mean(axis=1)

    missing_percentage = (
        numeric_data.isna().mean(axis=1) * 100
    )

    correlation = mean_abundance.corr(
        missing_percentage,
        method="spearman",
    )

    return float(correlation)





