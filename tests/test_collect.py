# Import campaign_data from marketing-data-pipeline-ai/src/collect.py
from src.collect import collect_campaign_data
# Import pandas for data manipulation
import pandas as pd

def test_collect_campaign_data():

    # Call collect_campaign_data to test it
    campaign_data = collect_campaign_data()
    # Test that campaign_data is a DataFrame
    assert isinstance(campaign_data, pd.DataFrame)
    # Test that campaign_data is not empty
    assert not campaign_data.empty
    # Test that the correct metrics are returned from collect_campaign_data
    assert set(["campaign", "impressions", "clicks", "conversions", "cost"]).issubset(campaign_data.columns)
