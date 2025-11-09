from src.Assignment_3.config.configuration import ConfigurationManager
from src.Assignment_3.components.Model_trainer import ModelTrainer
from src.Assignment_3 import logger

STAGE_NAME = "Model Trainer stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_tr_config = ModelTrainer(config=model_trainer_config)
        model_tr_config.train()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e