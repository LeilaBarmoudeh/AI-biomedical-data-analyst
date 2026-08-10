# Technical Roadmap

## AI Data Analyst for Biomedical Analytics

**Project duration:** 6 months  
**Project type:** Research and development pilot  
**Status:** In development

---

## 1. Purpose

The purpose of this roadmap is to define the technical development plan
for a six-month prototype of an external AI Data Analyst for biomedical
analytics.

The prototype will combine an external Python-based AI agent with Databricks, Large Language Model (LLM) services, MLflow, GitHub, and
Power BI.



---

## 2. Technical Vision

The system will follow a modular architecture:
```text
Researcher
    |
    v
External AI Data Analyst
(Python application)
    |
    +--------------------+--------------------+
    |                    |                    |
    v                    v                    v
Azure Databricks       LLM API             Power BI
    |                    |                    |
Data processing       Reasoning           Dashboards
Data quality          Tool selection      Visualization
Preprocessing         Interpretation      KPI reporting
Feature engineering   Report support
Statistics / ML
MLflow
    |
    v
Structured analytical results
    |
    v
External AI Data Analyst
    |
    v
Researcher Review
```

The AI Data Analyst will operate as an external orchestration layer.

Databricks will provide data engineering, analytical computation,
machine learning, and experiment tracking capabilities.

---

## 3. Core Technology Stack

### Development

- Python
- Visual Studio Code
- Git
- GitHub
- GitHub Copilot

### Data and Analytics Platform

- Databricks
- Python
- SQL
- Apache Spark where appropriate

### AI Layer

- Large Language Model API
- Structured outputs
- Tool/function calling
- Lightweight agent orchestration

### Model and Experiment Management

- MLflow

### Visualization and Reporting

- Power BI
- Python visualization libraries
- Markdown/structured reports

---

## 4. Six-Month MVP Scope

The MVP will focus on one external AI Data Analyst with a limited set
of analytical tools.

The prototype should be able to support:

1. Data ingestion
2. Data quality assessment
3. Data cleaning
4. Preprocessing
5. feature engineering
6. Exploratory data analysis
7. Selected statistical analyses
8. Selected machine-learning workflows
9. Retrieval of structured analytical results
10. LLM-assisted interpretation
11. Report generation
12. Dashboard-ready output
13. Human review and approval

The project will not attempt to build a fully autonomous or
production-grade multi-agent system.

---

# 5. Development Roadmap

## Month 1 — Foundation and Local Prototype

### Objectives

Establish the technical foundation and develop the first analytical
tools locally while Databricks access is being arranged.

### Tasks

- Finalize project vision
- Finalize system architecture
- Establish Git/GitHub workflow
- Configure Python development environment
- Select a public or synthetic biomedical demonstration dataset
- Define interfaces between the AI agent and analytical tools
- Develop initial data-quality functions
- Develop initial preprocessing functions
- Learn the fundamentals of LLM APIs
- Experiment with structured LLM outputs and tool calling

### Deliverables

- GitHub repository
- Technical documentation
- Reproducible Python environment
- Demonstration biomedical dataset
- Local data-quality module
- Initial LLM experiments

---

## Month 2 — Databricks Data Layer

### Objectives

Establish the cloud analytics layer and migrate or adapt the local
analytical tools to Databricks.

### Tasks

- Configure Azure Databricks workspace
- Connect Databricks with GitHub
- Import demonstration biomedical data
- Create raw and processed data layers
- Implement data-quality checks
- Implement cleaning workflows
- Implement preprocessing
- Implement basic feature engineering
- Document data transformations

### Deliverables

- Working Databricks environment
- Reproducible data ingestion pipeline
- Data-quality workflow
- Analysis-ready biomedical dataset
- Version-controlled Databricks code/notebooks

---

## Month 3 — Analytics and MLflow

### Objectives

Develop the analytical capabilities that the external AI agent will
later call.

### Tasks

- Implement exploratory data analysis
- Implement predefined statistical analysis tools
- Implement one or more simple machine-learning workflows
- Define standardized inputs and outputs for analytical functions
- Integrate MLflow experiment tracking
- Track parameters, metrics, and model versions
- Evaluate reproducibility of analytical workflows

### Deliverables

- Statistical analysis tools
- Initial ML workflow
- MLflow experiment tracking
- Structured analytical outputs
- Reproducible analytical pipeline

---

## Month 4 — External AI Data Analyst

### Objectives

Build the first working external AI Data Analyst.

### Tasks

- Implement LLM client
- Define system instructions
- Implement tool/function calling
- Connect the agent to selected analytical tools
- Enable the agent to request Databricks operations
- Return structured results to the agent
- Generate plain-language interpretations
- Add researcher confirmation for important analytical decisions
- Log agent actions for transparency

### Example workflow

Researcher:

"Check this dataset for potential data-quality problems."

AI Data Analyst:

1. Determines that a data-quality tool is required.
2. Calls the appropriate analytical service.
3. Receives structured results.
4. Interprets the results.
5. Presents findings and recommendations.
6. Waits for researcher approval before continuing.

### Deliverables

- Working external AI Data Analyst prototype
- Databricks integration
- Tool-calling workflow
- Human-in-the-loop controls
- Logged analytical decisions

---

## Month 5 — Visualization, Reporting and Integration

### Objectives

Connect analytical results with reporting and visualization.

### Tasks

- Generate dashboard-ready datasets
- Develop Power BI dashboard
- Generate analytical summaries
- Generate draft reports
- Integrate outputs from Databricks, the AI agent, and Power BI
- Test the complete workflow

### Deliverables

- Power BI dashboard
- Automated analytical summary
- Report-generation workflow
- End-to-end prototype

---

## Month 6 — Evaluation and Final Demonstration

### Objectives

Evaluate whether the AI-assisted workflow provides useful and reliable
support for biomedical analytics.

### Evaluation dimensions

#### Analytical correctness

Compare agent-supported outputs with manually verified analyses.

#### Reliability

Evaluate whether the agent selects appropriate predefined tools and
correctly communicates their outputs.

#### Reproducibility

Determine whether analyses can be reproduced from stored code,
configuration, data versions, and MLflow records.

#### Efficiency

Compare selected tasks performed manually versus with AI assistance.

#### Human oversight

Evaluate where researcher intervention remains necessary.

### Tasks

- Run end-to-end test scenarios
- Document failures and limitations
- Refine prompts and tools
- Evaluate analytical outputs
- Evaluate agent behavior
- Complete technical documentation
- Prepare GitHub portfolio presentation
- Prepare final project demonstration
- Collect feedback from research and industry collaborators

### Deliverables

- Evaluated AI Data Analyst prototype
- Final Power BI dashboard
- Technical report
- Evaluation results
- Documented limitations
- GitHub repository
- Demonstration/presentation

---

# 6. Development Principles

## Human-in-the-Loop

The system will assist researchers rather than independently make
scientific or clinical decisions.

Important analytical decisions will require human review.

## Reproducibility

Data transformations, analytical methods, model parameters, and agent
actions should be documented wherever practical.

## Modularity

Data processing, statistical analysis, AI reasoning, and visualization
will remain separate components.

## Structured Tool Use

The LLM should not perform numerical statistical calculations when a
validated analytical function can perform them instead.

The LLM will primarily be responsible for:

- understanding user requests
- selecting appropriate tools
- coordinating workflow
- interpreting structured results
- communicating results

## Data Protection

Development will initially use public, synthetic, or otherwise
appropriately approved biomedical datasets.

Sensitive or patient-level data will only be used within environments
approved for such data.

---

# 7. Initial Tool Set

The first AI Data Analyst will have a deliberately small tool set.

### Tool 1 — Data Quality

Checks:

- dimensions
- data types
- missing values
- duplicates
- suspicious values
- basic distributions

### Tool 2 — Preprocessing

Supports:

- missing-data handling
- transformations
- categorical encoding
- scaling where required

### Tool 3 — Exploratory Analysis

Produces:

- descriptive statistics
- distributions
- associations
- exploratory visualizations

### Tool 4 — Statistical Analysis

Initially supports a limited set of predefined methods.

Examples:

- group comparisons
- correlation
- linear regression
- logistic regression

### Tool 5 — Machine Learning

Initially supports a small number of predefined workflows with
appropriate evaluation metrics.

### Tool 6 — Reporting

Converts structured analytical outputs into a researcher-readable
summary.

---

# 8. Git and Development Workflow

GitHub will serve as the main source-code repository.

Development workflow:
```text
VS Code
    |
    v
Git
    |
    v
GitHub
    |
    +------> Azure Databricks
    |
    +------> Project documentation
```

GitHub Copilot will support software development but will not replace
code review, testing, or researcher validation.

Typical development cycle:

1. Create or modify a feature.
2. Test locally or in Databricks.
3. Review changes.
4. Commit using Git.
5. Push to GitHub.
6. Integrate tested changes into the prototype.

---

# 9. Key Risks and Mitigation

| Risk | Mitigation |
|---|---|
| Databricks access is delayed | Develop and test analytical modules locally first |
| Project scope becomes too large | Maintain strict MVP and postpone advanced features |
| LLM produces unreliable interpretations | Use structured outputs and validated analytical tools |
| Agent selects an inappropriate method | Restrict initial tool set and require researcher approval |
| API/cloud costs become excessive | Monitor usage and use small demonstration datasets |
| Sensitive biomedical data creates governance issues | Start with public or synthetic data |
| Integration becomes technically complex | Integrate components incrementally |
| Six-month timeline becomes restrictive | Prioritize one working end-to-end use case |

---

# 10. Out of Scope for the Six-Month Pilot

The following are explicitly outside the initial MVP:

- Fully autonomous scientific decision-making
- Clinical decision support
- Multi-agent architecture
- Training a Large Language Model from scratch
- Advanced LLM fine-tuning
- Large-scale production deployment
- Complex user authentication
- Real-time hospital system integration
- Autonomous modification of sensitive datasets
- Broad support for every statistical method

These may be considered as future extensions.

---

# 11. Success Criteria

The six-month pilot will be considered successful if:

1. A researcher can submit a supported analytical request to the
   external AI Data Analyst.
2. The agent can select an appropriate predefined analytical tool.
3. Azure Databricks can execute selected data or analytical operations.
4. Structured results can be returned to the external agent.
5. The agent can provide a useful interpretation of the results.
6. Results can be visualized or prepared for Power BI.
7. The workflow is reproducible and documented.
8. Important decisions remain under researcher control.

---

# 12. Future Extensions

If the six-month pilot demonstrates feasibility, future development may
include:

- additional statistical tools
- advanced ML workflows
- multiple specialized agents
- retrieval-augmented generation
- richer Databricks integration
- automated workflow monitoring
- advanced model/agent evaluation
- deployment as a web application
- additional biomedical use cases
- institutional deployment and governance