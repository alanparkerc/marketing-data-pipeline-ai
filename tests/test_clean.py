# Import clean_campaign_data from marketing-data-pipeline-ai/src/clean.py
from src.clean import clean_campaign_data
# Import pandas for data manipulation
import pandas as pd

def test_clean_campaign_data():

    # Test metrics (can be changed)
    raw_data = pd.DataFrame([{
        "campaign": "Test",
        "impressions": 1000,
        "clicks": 100,
        "conversions": 10,
        "cost": 200
    }])
    
    # Call clean_campaign_data with the test metrics to test it
    clean_data = clean_campaign_data(raw_data)
    # Test that CTR is in the clean output
    assert "CTR" in clean_data.columns
    # Test that CPC is in the clean output
    assert "CPC" in clean_data.columns
    # Test that CPL is in the clean output
    assert "CPL" in clean_data.columns
    # Test CTR is calculated correctly from clicks and impressions
    assert round(clean_data["CTR"].iloc[0], 4) == 0.1
    # Test CPC is calculated correctly from cost and clicks
    assert round(clean_data["CPC"].iloc[0], 2) == 2.0
    # Test CPL is calculated correctly from cost and conversions
    assert round(clean_data["CPL"].iloc[0], 2) == 20.0
