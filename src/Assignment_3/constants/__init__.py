from pathlib import Path

# Resolve paths relative to the project root so config files are found
# regardless of the current working directory when running scripts/notebooks.
# File layout (example):
#  <project_root>/src/Assignment_3/constants/__init__.py  <- this file
# Project root is three levels up from this file.
PROJECT_ROOT = Path(__file__).resolve().parents[3]

Config_yaml_path = PROJECT_ROOT / "config" / "config.yaml"
schema_yaml_path = PROJECT_ROOT / "schema.yaml"
params_yaml_path = PROJECT_ROOT / "params.yaml"