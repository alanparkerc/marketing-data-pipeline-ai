# Import generate_summary from marketing-data-pipeline-ai/src/llm_summary.py
from src.llm_summary import generate_summary
# Import pandas for data manipulation
import pandas as pd

def test_generate_summary():

    # Test marketing data used to generate the summary
    test_data = pd.DataFrame([{
        "campaign": "Mock",
        "impressions": 1000,
        "clicks": 50,
        "conversions": 5,
        "cost": 150
    }])

    # Call generate_summary with the test_data to test it    
    result = generate_summary(test_data)
    # Test if the resulting summary is a string
    assert isinstance(result, str)
