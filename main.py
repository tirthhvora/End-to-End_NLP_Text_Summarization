from TextSummarization.pipeline.step_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarization.logging import logger
from TextSummarization.pipeline.step_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


Stage_name = "Data Validation Stage"
try:
    logger.info(f"{Stage_name} Started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"{Stage_name} Completed")

except Exception as e:
    logger.exception(e)
    raise e
