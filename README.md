# This is a OPENAI-Powered Marketing Data Pipeline

This project is an automation pipeline written in Python that fetches marketing campaign data (currently test data), calculates key performance metrics, summarizes the trends in the data using ChatGPT, and exports the results to CSV and JSON, while sending an email with results to the user.

# Current Features
- A small test campaign data collection (will be replaced with real APIs)
- Computes KPIs such as CTR, CPC, and CPL (or Cost Per Conversion)
- Generates campaign summaries using ChatGPT
- Exports that data as CSV/JSON
- Testing Suite

## Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Create a `.env` file
```
OPENAI_API_KEY=your_openai_key
EMAIL_SENDER=sender@example.com
EMAIL_RECIPIENT=recipient@example.com
SMTP_SERVER=smtp.yourprovider.com
SMTP_PORT=587
SMTP_USER=user@example.com
SMTP_PASSWORD=email_password
```

### 3. Run the pipeline
```bash
python main.py
```

## ✅ Running Tests
```bash
pytest tests/
```
Tests cover:
- KPI calculations
- LLM summary output (mocked in test mode)
- CSV/JSON export file creation

## Plans For The Future
- Integrate Google/Facebook Ads APIs
- Add dashboard
- Deploy to cron scheduler
