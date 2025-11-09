from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir : Path
    local_data_file : Path


from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen = True)
class DataValidationConfig:
    root_dir : Path
    STATUS_FILE : str
    all_schema: dict



@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    n_estimators: int
    criterion: str
    max_depth: int
    min_samples_split: int
    min_samples_leaf: int
    min_weight_fraction_leaf: float
    max_features: str
    max_leaf_nodes: int
    min_impurity_decrease: float
    bootstrap: str
    oob_score: str
    n_jobs: int
    random_state: int
    verbose: int
    warm_start: str
    class_weight: int
    ccp_alpha: float
    max_samples: int
    monotonic_cst: int
    target_column: str
    params : any


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str






