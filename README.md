* AI Data Analyst for Biomedical Analytics *

## Project Overview

This project explores how an external AI agent can support researchers
throughout the biomedical data analysis workflow.

The goal is to develop a lightweight **AI Data Analyst** that can
coordinate selected analytical tasks across data processing, statistical
analysis, machine learning, interpretation, and reporting.

Rather than embedding the agent within a single analytics platform, the
AI Data Analyst is designed as an **external orchestration layer** that
can interact with analytical services such as  Databricks, LLM
services, MLflow, and visualization tools.

The project is being developed as a six-month research and development prototype.

---

## Motivation

Biomedical data analysis often involves multiple interconnected steps,
including:

- data ingestion
- data quality assessment
- cleaning and preprocessing
- exploratory data analysis
- statistical analysis
- machine learning
- model evaluation
- interpretation
- visualization and reporting

These activities often require researchers to move between different
tools and environments.

This project investigates whether an AI agent can act as an intelligent
coordination layer between these tools while keeping the researcher in
control of analytical decisions.

---

## Proposed Architecture

The planned system follows the architecture:
```text
Researcher

↓

External AI Data Analyst

↓

Tool selection and workflow orchestration

↓

Azure Databricks / Analytical Tools

↓

Structured analytical results

↓

LLM-assisted interpretation

↓

Power BI / Analytical Report

↓

Researcher Review
```

The AI agent will not independently make scientific or clinical
decisions. Human review remains part of the workflow.

---

## Biomedical Use Case

The primary demonstration case is a publicly available hepatocellular
carcinoma (HCC) multi-omics dataset containing:

- RNA-seq data
- proteomics data
- phosphoproteomics data
- paired tumor and adjacent-normal samples

The project will begin with a simplified single-omics workflow and
progressively extend toward more complex paired and multi-omics
analyses.

### Data Source

HCC multi-omics dataset:

https://zenodo.org/records/14553766

Associated publication:

**Integrated Proteogenomic Characterization of HBV-Related
Hepatocellular Carcinoma**

Cell (2019)

https://pubmed.ncbi.nlm.nih.gov/31585088/

Raw biomedical data are not stored directly in this repository.

---

## Planned AI Data Analyst Capabilities

The six-month MVP will focus on a limited set of well-defined
capabilities:

1. Data quality assessment
2. Data cleaning and preprocessing
3. Exploratory data analysis
4. Selected statistical analyses
5. Selected machine-learning workflows
6. Retrieval of structured analytical results
7. LLM-assisted interpretation
8. Report generation
9. Dashboard-ready outputs
10. Human review and approval

The objective is not to create a fully autonomous data scientist, but
to evaluate how an AI agent can support and coordinate a realistic
biomedical analytics workflow.

---

## Technology Stack

### Development
- Python
- Visual Studio Code
- Git
- GitHub
- GitHub Copilot

### Data and Analytics
- Azure Databricks
- Python
- SQL
- Apache Spark where appropriate

### AI
- Large Language Model API
- Tool/function calling
- Structured outputs
- Lightweight agent orchestration

### Experiment Tracking and Evaluation
- MLflow

### Visualization
- Power BI
- Python visualization libraries

---

## Development Roadmap

The project is organized into six main phases:

### Phase 1 — Foundation
Project architecture, development environment, biomedical data
preparation, and initial data-quality tools.

### Phase 2 — Databricks Data Layer
Data ingestion, quality assessment, cleaning, preprocessing, and
feature engineering.

### Phase 3 — Analytics and MLflow
Statistical analysis, machine-learning workflows, structured analytical
outputs, and experiment tracking.

### Phase 4 — External AI Data Analyst
LLM integration, tool selection, Databricks interaction, interpretation,
and human-in-the-loop controls.

### Phase 5 — Visualization and Reporting
Power BI integration, analytical summaries, and end-to-end workflow.

### Phase 6 — Evaluation
Evaluation of analytical correctness, reliability, reproducibility,
efficiency, and limitations.

More details are available in:

`docs/technical_roadmap.md`

---

## Current Pipeline

### 1. Data Understanding and Quality Assessment

The pipeline performs automated checks including:

- Dataset dimensions
- Numeric type validation
- Duplicate identifiers
- Duplicate sample names
- Missing-value assessment
- Fully missing features
- Constant features
- Basic distribution statistics

The reusable implementation is located in:

```text
src/data_quality/
```

### 2. Missingness Analysis and Preprocessing

Feature-level and sample-level missingness are evaluated before imputation.

Features with more than **30% missing values** are removed.

For the current proteomics dataset:

| Metric | Result |
|---|---:|
| Original proteins | 11,175 |
| Retained proteins | 8,368 |
| Removed proteins | 2,807 |
| Remaining missingness | 2.37% |

The relationship between protein abundance and missingness is also assessed using Spearman correlation.

Observed correlation:

```text
Spearman rho ≈ -0.605
```

This indicates a substantial abundance-associated missingness pattern: lower-abundance proteins tend to have more missing observations. This association is treated as a diagnostic rather than proof of a specific missing-data mechanism.

### 3. Imputation Evaluation

Imputation methods are evaluated using artificial masking of observed values.

The validation workflow is:

```text
Observed Data
      ↓
Artificially Mask Known Values
      ↓
Apply Imputation
      ↓
Compare Imputed vs True Values
      ↓
MAE / RMSE
```

This makes it possible to evaluate imputation performance objectively because the true values of the artificially masked observations are known.

### 4. Median Imputation Baseline

Median imputation is used as the baseline method.

Current validation performance:

| Method | MAE | RMSE |
|---|---:|---:|
| Median | 0.2068 | 0.3105 |

### 5. Automated KNN Imputation

Rather than fixing the number of neighbors manually, the pipeline automatically evaluates candidate values of `k`.

Candidate values are generated according to the number of samples and evaluated using repeated artificial-masking experiments.

For the current dataset, repeated validation selected:

```text
Optimal k = 5
```

Performance across five validation runs:

| k | Mean MAE | Mean RMSE | RMSE SD |
|---:|---:|---:|---:|
| **5** | **0.1580** | **0.2417** | **0.0011** |
| 7 | 0.1586 | 0.2423 | 0.0011 |
| 9 | 0.1602 | 0.2448 | 0.0011 |
| 11 | 0.1618 | 0.2474 | 0.0012 |
| 3 | 0.1621 | 0.2482 | 0.0018 |
| 12 | 0.1626 | 0.2486 | 0.0012 |

KNN currently outperforms the median baseline under random-masking validation.

Importantly, the selected value of `k` is **dataset-dependent**. The pipeline therefore performs automatic validation rather than permanently setting `k=5`.

## Repository Structure

```text
ai-analytics-agent/
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_imputation_evaluation.ipynb
│
├── src/
│   ├── data_quality/
│   │   └── quality_checker.py
│   │
│   ├── preprocessing/
│   │   └── preprocessing.py
│   │
│   └── imputation/
│       └── imputation.py
│
├── tests/
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Design Principle

The project separates exploratory notebooks from reusable analytical components.

**Notebooks** are used for:

- Exploration
- Visualization
- Interpretation
- Experimental validation

**Python modules** contain reusable functions that can eventually be called by the AI Data Analyst.

This separation is intended to make the workflow reproducible, testable, and suitable for future automation.

## Technology Stack

- Python
- Pandas
- NumPy
- scikit-learn
- Jupyter
- Git / GitHub
- Azure Databricks
- MLflow
- Power BI
- LLM integration (planned)

## Current Development Status

Completed:

- Data-quality framework
- Numeric validation
- Missingness analysis
- Sparse-feature filtering
- Median imputation
- Artificial-masking validation framework
- MAE/RMSE evaluation
- KNN imputation
- Automatic KNN hyperparameter selection
- Repeated validation across random masks

In progress / planned:

- Additional imputation strategies
- Automated comparison of imputation methods
- Statistical analysis modules
- MLflow experiment tracking
- Azure Databricks integration
- AI Data Analyst orchestration
- LLM-based analytical reasoning
- Power BI reporting
- Human-in-the-loop analytical review

## Project Goal

The final system aims to support a workflow in which an AI assistant can:

1. Inspect incoming data.
2. Identify data-quality problems.
3. Recommend appropriate preprocessing strategies.
4. Evaluate alternative analytical methods.
5. Execute approved analytical tools.
6. Explain results and methodological choices.
7. Generate structured outputs for reporting and visualization.

The objective is **AI-assisted analytics rather than autonomous decision-making**: analytical recommendations remain transparent and subject to human review.

## Status

 **Active development — 2026**

This repository currently represents an evolving research and portfolio prototype.
---

## Repository Structure

```text
ai-analytics-agent/
│
├── data/
│
├── docs/
│   ├── project_vision.md
│   ├── system_architecture.md
│   └── technical_roadmap.md
│
├── src/
│
├── .gitignore
├── README.md
└── requirements.txt