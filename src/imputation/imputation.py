import numpy as np
import pandas as pd

from sklearn.impute import KNNImputer


def median_imputation(
    df: pd.DataFrame,
    id_column: str = "idx",
) -> pd.DataFrame:
    """
    Impute missing values using the median value of each feature.

    Features are rows and samples are columns.
    """
    if id_column not in df.columns:
        raise ValueError(
            f"Identifier column '{id_column}' was not found."
        )

    result = df.copy()

    sample_columns = [
        column for column in result.columns
        if column != id_column
    ]

    numeric_data = result[sample_columns].apply(
        pd.to_numeric,
        errors="coerce",
    )

    feature_medians = numeric_data.median(axis=1)

    numeric_data = numeric_data.T.fillna(feature_medians).T

    result[sample_columns] = numeric_data

    return result


import numpy as np
import pandas as pd


def create_random_mask(
    df: pd.DataFrame,
    id_column: str = "idx",
    mask_fraction: float = 0.05,
    random_state: int = 42,
):
    """
    Artificially mask a fraction of observed values for
    imputation validation.

    Only originally observed values are eligible for masking.

    Returns
    -------
    masked_df:
        Copy of the dataframe with selected observed values
        replaced by NaN.

    mask:
        Boolean DataFrame identifying artificially masked values.

    true_values:
        Original numeric data before artificial masking.
    """

    if id_column not in df.columns:
        raise ValueError(
            f"Identifier column '{id_column}' was not found."
        )

    if not 0 < mask_fraction < 1:
        raise ValueError(
            "mask_fraction must be between 0 and 1."
        )

    result = df.copy()

    sample_columns = [
        col for col in result.columns
        if col != id_column
    ]

    numeric_data = result[sample_columns].apply(
        pd.to_numeric,
        errors="coerce",
    )

    true_values = numeric_data.copy()

    # Only observed values may be artificially hidden
    observed_positions = np.argwhere(
        numeric_data.notna().to_numpy()
    )

    rng = np.random.default_rng(random_state)

    n_mask = int(
        len(observed_positions) * mask_fraction
    )

    selected = rng.choice(
        len(observed_positions),
        size=n_mask,
        replace=False,
    )

    selected_positions = observed_positions[selected]

    mask = pd.DataFrame(
        False,
        index=numeric_data.index,
        columns=numeric_data.columns,
    )

    for row, col in selected_positions:
        mask.iat[row, col] = True
        numeric_data.iat[row, col] = np.nan

    result[sample_columns] = numeric_data

    return result, mask, true_values


import numpy as np
import pandas as pd


def evaluate_imputation(
    imputed_df: pd.DataFrame,
    true_values: pd.DataFrame,
    validation_mask: pd.DataFrame,
    id_column: str = "idx",
) -> dict:
    """
    Evaluate imputation accuracy on artificially masked values.

    Returns MAE and RMSE.
    """

    sample_columns = [
        col for col in imputed_df.columns
        if col != id_column
    ]

    imputed_values = (
        imputed_df[sample_columns]
        .apply(pd.to_numeric, errors="coerce")
    )

    y_true = true_values.to_numpy()[validation_mask.to_numpy()]
    y_pred = imputed_values.to_numpy()[validation_mask.to_numpy()]

    mae = np.mean(np.abs(y_true - y_pred))

    rmse = np.sqrt(
        np.mean((y_true - y_pred) ** 2)
    )

    return {
        "MAE": float(mae),
        "RMSE": float(rmse),
        "n_evaluated": int(len(y_true)),
    }


from sklearn.impute import KNNImputer


def knn_imputation(
    df: pd.DataFrame,
    id_column: str = "idx",
    n_neighbors: int = 5,
) -> pd.DataFrame:
    """
    Impute missing values using K-nearest-neighbor samples.

    The input contains proteins as rows and samples as columns.
    The matrix is transposed so that samples are observations
    and proteins are features for KNN imputation.
    """
    if id_column not in df.columns:
        raise ValueError(
            f"Identifier column '{id_column}' was not found."
        )

    result = df.copy()

    sample_columns = [
        col for col in result.columns
        if col != id_column
    ]

    numeric_data = result[sample_columns].apply(
        pd.to_numeric,
        errors="coerce",
    )

    # Samples × proteins
    transposed = numeric_data.T

    imputer = KNNImputer(
        n_neighbors=n_neighbors,
        weights="distance",
    )

    imputed_array = imputer.fit_transform(transposed)

    imputed_data = pd.DataFrame(
        imputed_array,
        index=transposed.index,
        columns=transposed.columns,
    ).T

    result[sample_columns] = imputed_data

    return result



def repeated_knn_validation(
    df: pd.DataFrame,
    id_column: str = "idx",
    mask_fraction: float = 0.05,
    random_states=None,
) -> tuple[int, pd.DataFrame, pd.DataFrame]:
    """
    Repeatedly evaluate KNN imputation across several artificial masks.

    Returns
    -------
    best_k:
        K value with the lowest mean RMSE.

    summary_df:
        Mean and standard deviation of MAE/RMSE for each k.

    detailed_df:
        Results for every random seed and k.
    """

    if random_states is None:
        random_states = [42, 123, 456, 789, 2026]

    sample_columns = [
        col for col in df.columns
        if col != id_column
    ]

    n_samples = len(sample_columns)

    max_k = min(
        20,
        max(3, int(np.sqrt(n_samples)))
    )

    candidate_k = list(
        range(3, max_k + 1, 2)
    )

    if max_k not in candidate_k:
        candidate_k.append(max_k)

    candidate_k = sorted(set(candidate_k))

    all_results = []

    for seed in random_states:

        df_masked, validation_mask, true_values = create_random_mask(
            df=df,
            id_column=id_column,
            mask_fraction=mask_fraction,
            random_state=seed,
        )

        for k in candidate_k:

            df_imputed = knn_imputation(
                df=df_masked,
                id_column=id_column,
                n_neighbors=k,
            )

            metrics = evaluate_imputation(
                imputed_df=df_imputed,
                true_values=true_values,
                validation_mask=validation_mask,
                id_column=id_column,
            )

            all_results.append(
                {
                    "random_state": seed,
                    "k": k,
                    "MAE": metrics["MAE"],
                    "RMSE": metrics["RMSE"],
                    "n_evaluated": metrics["n_evaluated"],
                }
            )

    detailed_df = pd.DataFrame(all_results)

    summary_df = (
        detailed_df
        .groupby("k")
        .agg(
            mean_MAE=("MAE", "mean"),
            std_MAE=("MAE", "std"),
            mean_RMSE=("RMSE", "mean"),
            std_RMSE=("RMSE", "std"),
            n_runs=("RMSE", "count"),
        )
        .reset_index()
        .sort_values("mean_RMSE")
        .reset_index(drop=True)
    )

    best_k = int(
        summary_df.loc[0, "k"]
    )

    return best_k, summary_df, detailed_df




