# System Architecture#

# 1. Purpose#

The purpose of the system is to develop a prototype AI Data Analyst that supports researchers across key stages of the biomedical data
analytics lifecycle.

The system will combine a cloud data platform, traditional analytical
tools, and a Large Language Model to support data preparation,
analysis, visualization, and reporting while maintaining human
oversight.

# 2. High-Level Architecture#

Biomedical Data
        |
        v
Databricks
        |
        |-- Data ingestion
        |-- Data quality
        |-- Cleaning
        |-- Preprocessing
        |-- Feature engineering
        |
        v
AI Data Analyst
(Python application developed in VS Code)
        |
        |-- LLM reasoning
        |-- Tool selection
        |-- Statistical analysis
        |-- Interpretation
        |-- Report generation
        |
        v
Power BI
        |
        |-- Dashboard
        |-- Visualization
        |-- KPI reporting
        |
        v
Researcher Review

# 3. Development Environment#

# VS Code#
Main software development environment.

# GitHub#
Version control, documentation, and project portfolio.

# GitHub Copilot #
AI-assisted coding, testing, refactoring, and documentation.

### Databricks
Cloud data platform for data ingestion, preparation, processing, and experiment tracking.

# Python #
Core language for the AI Data Analyst application.

# SQL #
Data querying and transformation.

# LLM API #
Provides reasoning and natural-language interaction capabilities.

# Power BI #
Dashboarding and communication of analytical results.

# 4. Human-in-the-Loop Principle #

The AI Data Analyst will not independently make scientific or clinical decisions.

The researcher remains responsible for reviewing and approving:

- data-cleaning decisions
- preprocessing decisions
- statistical methods
- model results
- interpretations
- final reports


## 5. Six-Month MVP

The first prototype should be able to:

1. Access a biomedical dataset.
2. Assess basic data quality.
3. Support data cleaning and preprocessing.
4. Generate exploratory data analysis.
5. Perform selected statistical analyses.
6. Prepare data/results for visualization and dashboards.
7. Generate an analytical summary/report.
8. Allow the researcher to review the outputs.

