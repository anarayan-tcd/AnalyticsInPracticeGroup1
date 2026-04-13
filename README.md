# Telco Customer Churn - Analytics in Practice Group 1 Project
This project simulates a real-world analytics consulting engagement. We act as a data analytics firm hired by a telecom company to analyse customer churn. Using the Telco Customer Churn dataset, we identify the reasons customers leave and provide business recommendations to reduce churn.

**Deadline: 16th April 2026 Format: PowerPoint Presentation + Github Repo**

## Team Members and Roles
| Name | Surname | Email | Role |
|------|---------|-------|------|
| Nicole | Kuzmetova | KUZMETON@TCD.IE | Project Manager / Storyteller |
| Shiva | Ulaganathan Chidambaram | ULAGANAS@TCD.IE | Project Manager / Storyteller |
| Shu Min | Lim | LIMS6@TCD.IE | LLM Prompt Specialist |
| Soumik | Ghoshal | GHOSHALS@TCD.IE | LLM Prompt Specialist |
| Aditya | Narayan | ANARAYAN@TCD.IE | Modeler / Analyst |
| Vanessa | Martinez Marin | MARTIJ21@TCD.IE | Modeler / Analyst |
| Nga Yin | Hui | HUIN@TCD.IE | Data Engineer |
| Xingming | Li | LIX35@TCD.IE | Data Engineer |
| Shuaiya | Xiong | SHXIONG@TCD.IE | Visualization Expert |
| Nadia | El-Fakih | ELFAKIHN@TCD.IE | Visualization Expert |

## Timeline 
| Date | What's Happening |
|------|-----------------|
| 7th - 8th April | Data Engineers clean and load the dataset. Full team reviews research questions. |
| 9th - 10th April | Modelers run EDA and build models. LLM Specialists start designing prompts. Viz team plans charts. |
| 11th - 12th April | Viz team builds all charts. LLM Specialists log and critique outputs. Project Managers draft slides 1, 7, 8, and 10. |
| 13th April | Everyone sends their slides to the Project Managers. PM team assembles the full deck. |
| 14th April | Full team reviews presentation. Fix issues. Check all references and AI acknowledgements. |
| 15th April | Final push to GitHub. Presentation polished and ready. |
| 16th April | Deadline |

## Research Questions
- Do customers without online security/antivirus churn more?
- Does having cloud backup make customers more likely to stay?
- Do customers who use streaming services (TV & movies) churn less?
- Which customers are most at risk of churning, and what should the company do about it?

## Dataset
- **Source:** Telco Customer Churn - Kaggle (available in the Repo)
- **Description:** Contains data on 7,000+ telecom customers, including tenure, services used, monthly charges, and whether they churned.
- **File Used:** WA_Fn-UseC_-Telco-Customer-Churn.csv 

## Folder Structure 
```
AnalyticsInPracticeGroup1/
│
├── data/                          # Raw and cleaned datasets
├── data_engineering/              # Cleaning pipeline and scripts 
├── data_analytics/                # Clustering, correlation analysis, logistic regression
├── eda_modeling/                  # EDA and predictive modelling notebooks 
├── visualisations/                # Final charts for presentation 
├── LICENSE
└── README.md
```
## How To Run 

1. Clone the repo:
```bash
git clone https://github.com/anarayan-tcd/AnalyticsInPracticeGroup1.git
```

2. Install required libraries:
```bash
pip install pandas scikit-learn xgboost matplotlib seaborn jupyter
```

3. Run the data cleaning pipeline:
```bash
python DataCleanPipeline.py
```
*Windows users: simply double-click `run_pipeline.bat`*

4. Open the analysis notebooks in the `Data Analytics` and `EDA Modeling` folders using Jupyter Notebook or Python.

---

## LLM Prompt Log (LLM specialists have to fill out)

The team used Gemini 1.5 Pro to audit and critique the technical work at three key stages
of the project. All outputs were reviewed and verified by the team before inclusion.

| # | Prompt | Input | Key Output |
|---|--------|-------|------------|
| 1 | Data Pipeline Critique | DataCleanPipeline.py | Confirmed pipeline is safe and well-modularised. Flagged missing feature scaling and outlier detection. |
| 2 | Model Reliability Assessment | logistic_regression_results.csv | Identified that 49% of churners are missed (recall 0.51) — a significant business risk. |
| 3 | Insight Synthesis for Recommendations | Model coefficients | Translated top 3 churn drivers into CEO-ready strategies with business caveats. |

**Additional AI use: Claude was used to generate a cluster visualisation and 40 synthetic test customer profiles based on the clustering results.

Full prompt details, inputs, outputs and assessments are documented in each team member's folder README.

## Models used
Six machine learning models were trained and evaluated:

| Model | Notes |
|-------|-------|
| Logistic Regression | Best for interpretability per research question |
| Decision Tree | Baseline comparison |
| Random Forest | Confirms feature importance |
| Gradient Boosting | Best overall model (ROC AUC = 0.8470) |
| XGBoost | Strong churn ranking, SHAP values |
| K-Nearest Neighbours | Comparison model |

**Validation approach:** 80/20 train-test split with stratification + 5-fold cross-validation via GridSearchCV for hyperparameter tuning.

## References (add later)

## Gen AI Acknowledgement 
- This project used generative AI tools to support the research and development process.
- AI was used to assist with code generation, data interpretation, and summarising findings. 
- All AI-generated content was reviewed, verified, and edited by team members before inclusion.  

Final analysis, conclusions, and recommendations reflect the team's own judgment.
AI tools used: ChatGPT, Claude


