# 🌲 ML Assignment 3 — pipeline

This repository builds and evaluates a **machine learning pipeline** for predicting forest cover type using cartographic variables.
It automates data ingestion, validation, transformation, model training, and evaluation — all driven by YAML configurations.

### What’s included

#### 🧩 Root files

* **main.py** — orchestrates the full end-to-end pipeline (runs all stages sequentially)
* **params.yaml** — stores model hyperparameters
* **config.yaml** — controls file paths and component settings
* **schema.yaml** — defines the input dataset structure for validation
* **requirements.txt** — dependencies list
* **README.md** — project overview and workflow

---

#### 📦 src/ — main project modules

| File / Folder   | Description                                                                       |
| --------------- | --------------------------------------------------------------------------------- |
| **components/** | Each pipeline stage — ingestion, validation, transformation, training, evaluation |
| **config/**     | Configuration manager for loading YAML settings dynamically                       |
| **constants/**  | Global constants (paths, schema references, etc.)                                 |
| **entity/**     | Data classes for configuration and artifact entities                              |
| **pipeline/**   | Wrapper scripts to run each ML pipeline stage                                     |
| **utils/**      | Helper functions for saving models, reading YAMLs, etc.                           |

---

#### 🗂 artifacts/ — runtime outputs

Created automatically when you run `main.py`.
Stores:

* Intermediate datasets (`train.csv`, `test.csv`)
* Trained model file (`model.joblib`)
* Evaluation results (`metrics.json`)
* Logs and status reports

---

#### 🧠 research/

Experimental Jupyter notebooks for testing data loading, transformations, and model behavior before formalizing them into the pipeline.

---

#### 🪵 logs/

Contains structured runtime logs for debugging and audit trails.

---

### Quick setup

**PowerShell**

```powershell
# Create virtual environment
python -m venv .venv; .\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

Ensure the dataset exists under `Data/covertype/` (for example, `Data/covertype/covtype.data`).

---

### Run the full pipeline

This executes data ingestion → validation → transformation → training → evaluation automatically.

**PowerShell**

```powershell
python main.py
```

**Outputs:**

* Processed data → `artifacts/data_transformation/`
* Model → `artifacts/model_trainer/model.joblib`
* Evaluation metrics → `artifacts/model_evaluation/metrics.json`

---

### Logging behavior

All logs are written to the `logs/` directory automatically during each pipeline run.

Typical structure:

```
logs/
├── running_log.log    # standard runtime logs
└── error_log.log      # optional error details if implemented
```

---

### Troubleshooting

| Issue                                  | Fix                                                                      |
| -------------------------------------- | ------------------------------------------------------------------------ |
| **Git push fails (large file >100MB)** | Use Git LFS or remove heavy artifacts before pushing                     |
| **File path issues (Windows)**         | Use raw string paths, e.g., `r"C:\Users\..."`                            |
| **Model not saving**                   | Check artifact directory permissions and relative paths in `config.yaml` |
| **Module import errors**               | Verify you’re running from project root: `python main.py`                |

---

### Notes

* Each stage runs independently, so you can test modules individually (e.g., run only Data Transformation or Model Training).
* YAML-driven design allows changing file paths, model parameters, or schema without editing code.
* The modular setup makes it simple to extend with new algorithms, cross-validation, or cloud integrations later.
