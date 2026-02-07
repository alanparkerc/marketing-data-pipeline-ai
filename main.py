# Use dotenv to load .env on start
from dotenv import load_dotenv
load_dotenv()

import logging
# Import collect_campaign_data from marketing-data-pipeline-ai/src/collect.py
from src.collect import collect_campaign_data
# Import clean_campaign_data from marketing-data-pipeline-ai/src/clean.py
from src.clean import clean_campaign_data
# Import generate_summary from marketing-data-pipeline-ai/src/llm_summary.py
from src.llm_summary import generate_summary
# Import export_to_csv and export_to_json from marketing-data-pipeline-ai/src/export.py
from src.export import export_to_csv, export_to_json
# Import send_email_report from marketing-data-pipeline-ai/src/email_report.py
from src.email_report import send_email_report

def run_pipeline():

    # Initialize logging with basic logging configuration
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting data pipeline...")

    # calling collect_campaign_data() from marketing-data-pipeline-ai/src/collect.py to retrieve raw_data
    raw_data = collect_campaign_data()
    # calling clean_campaign_data and passing the raw data to clean the raw campaign data and return the KPI metrics under clean_data
    clean_data = clean_campaign_data(raw_data)
    # calling generate_summary and passing the clean data to generate a summary and return it to the summary variable
    summary = generate_summary(clean_data)

    # calling export_to_csv and export_to_json and passing the clean_data and file path in order to export the clean data to CSV and JSON formats in the data folder
    export_to_csv(clean_data, "data/clean_data.csv")
    export_to_json(clean_data, "data/clean_data.json")

    # calling send_email_report and passing the summary to send the generated summary by email
    send_email_report(summary)

    # Logging the successful completion of the pipeline run
    logging.info("Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()
