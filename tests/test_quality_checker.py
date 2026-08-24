import pandas as pd

from src.data_quality.quality_checker import data_quality_report


def test_data_quality_report() -> None:
    df = pd.DataFrame(
        {
            "idx": ["gene_1", "gene_2", "gene_3"],
            "sample_1": [1.0, 2.0, None],
            "sample_2": [1.5, 2.5, 3.5],
        }
    )

    report = data_quality_report(df)

    metrics = dict(zip(report["Metric"], report["Value"]))

    assert metrics["Number of features"] == 3
    assert metrics["Number of samples"] == 2
    assert metrics["Total missing values"] == 1
    assert metrics["Duplicate identifiers"] == 0
    