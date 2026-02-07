# Import pandas for data manipulation
import pandas as pd
import datetime

def collect_campaign_data():

    # Retrieve today's date
    today = datetime.date.today()
    # Current test data that represents example output from Google or Facebook ads
    data = [
        {"date": today, "campaign": "Brand Awareness", "impressions": 12000, "clicks": 300, "conversions": 25, "cost": 450.00},
        {"date": today, "campaign": "Lead Gen", "impressions": 9000, "clicks": 500, "conversions": 45, "cost": 390.00},
        {"date": today, "campaign": "Retargeting", "impressions": 5000, "clicks": 200, "conversions": 40, "cost": 320.00}
    ]
    # Frame the data as a DataFrame
    campaign_data = pd.DataFrame(data)
    # Return new DataFrame formatted data
    return campaign_data
