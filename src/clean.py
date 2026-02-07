# Import pandas for data manipulation
import pandas as pd

# Imports campaign_data to clean
def clean_campaign_data(campaign_data):
    
    # Save copy of campaign_data within clean.py so it has it's own copy
    campaign_data = campaign_data.copy()
    
    # Computes example marketing KPIs such as:
    # CPL (Cost Per Lead or Cost Per Conversion)
    # CPC (Cost Per Click)
    # CTR (Clicks Through Rate or Clicks Per Impression)
    # Avoids divide-by-zero operations by replacing 0 with NaN if that is the case
    campaign_data["CPL"] = campaign_data["cost"] / campaign_data["conversions"].replace({0: pd.NA})
    campaign_data["CPC"] = campaign_data["cost"] / campaign_data["clicks"].replace({0: pd.NA})
    campaign_data["CTR"] = campaign_data["clicks"] / campaign_data["impressions"].replace({0: pd.NA})

    # Round out values appropriately
    # CPL and CPC rounded to nearest hundredth
    # CTR rouned to the nearest ten-thousandth
    campaign_data["CPL"] = campaign_data["CPL"].round(2)
    campaign_data["CPC"] = campaign_data["CPC"].round(2)
    campaign_data["CTR"] = campaign_data["CTR"].round(4)

    return campaign_data
