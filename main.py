from TextSummarization.pipeline.step_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarization.logging import logger

Stage_name = "Data Ingestion Stage"
try:
    logger.info(f"{Stage_name} Started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{Stage_name} Completed")

except Exception as e:
    logger.exception(e)
    raise e
