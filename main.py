from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline

STAGE_NAME = "DATA INGESTION STAGE"
try:
    logger.info(f"------> stage {STAGE_NAME} started <------\n\n")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"------> stage {STAGE_NAME} ended <------\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "PREPARE BASE MODEL"
try:
    logger.info(f"------> stage {STAGE_NAME} started <------\n\n")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f"------> stage {STAGE_NAME} ended <------\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "TRAINING THE MODEL"
try:
        logger.info(f"======")
        logger.info(f"------> stage {STAGE_NAME} started <------")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"------> stage {STAGE_NAME} ended <------\n\n======")
except Exception as e:
    logger.exception(e)
    raise e