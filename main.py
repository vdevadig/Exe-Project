from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "DATA INGESTION STAGE"
try:
    logger.info(f"------> stage {STAGE_NAME} started <------\n\n")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"------> stage {STAGE_NAME} ended <------\n\n")
except Exception as e:
    logger.exception(e)
    raise e