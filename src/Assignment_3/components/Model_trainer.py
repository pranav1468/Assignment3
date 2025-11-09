from src.Assignment_3 import logger
import pandas as pd
import urllib.request as request
from src.Assignment_3 import logger
from src.Assignment_3.utils.common import get_size
from src.Assignment_3.entity.config_entity import *
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
import joblib
from sklearn.ensemble import RandomForestClassifier

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)

        # ✅ FIX: use 1D Series
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]

        # ✅ FIX: correct params reference
        params = self.config.params.RandomForestClassifier


        rf = RandomForestClassifier(
            n_estimators = params.n_estimators,
            criterion = params.criterion,
            max_depth = params.max_depth,
            min_samples_split = params.min_samples_split,
            min_samples_leaf = params.min_samples_leaf,
            min_weight_fraction_leaf = params.min_weight_fraction_leaf,
            max_features = params.max_features,
            max_leaf_nodes = params.max_leaf_nodes,
            min_impurity_decrease = params.min_impurity_decrease,
            bootstrap = params.bootstrap,
            oob_score = params.oob_score,
            n_jobs = params.n_jobs,
            random_state = params.random_state,
            verbose = params.verbose,
            warm_start = params.warm_start,
            class_weight = params.class_weight,
            ccp_alpha = params.ccp_alpha,
            max_samples = params.max_samples,
            monotonic_cst = params.monotonic_cst,
        )

        # ✅ FIX: y must be 1D
        rf.fit(train_x, train_y)

        joblib.dump(rf, os.path.join(self.config.root_dir, self.config.model_name))
