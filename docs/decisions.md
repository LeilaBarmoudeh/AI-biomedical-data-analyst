# Technical Decisions

## External AI Agent

The AI Data Analyst will be developed as an external Python application
rather than as an agent embedded entirely inside Databricks.

## Azure Databricks

Azure Databricks will provide data ingestion, transformation,
preprocessing, statistical and machine-learning execution, and MLflow
tracking.

## Development Environment

VS Code will be used for software development. GitHub will serve as the
main source-code repository.

## Notebook and Module Separation

Jupyter notebooks will be used for exploration and validation. Stable,
reusable functionality will be moved into Python modules under `src/`.

## Biomedical Use Case

The public HCC multi-omics dataset will be used as the primary
demonstration case. Development begins with the Normal proteomics
matrix.