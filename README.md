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

## Current Status

**Project status: In development**

Current work focuses on:

- project architecture
- reproducible Python environment
- preparation of the HCC use case
- development of the first data-quality module

Azure Databricks integration will be added once the required workspace
access is available.

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