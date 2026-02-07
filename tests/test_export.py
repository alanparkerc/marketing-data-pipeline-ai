# Import export_to_csv and export_to_json from marketing-data-pipeline-ai/src/export.py
from src.export import export_to_csv, export_to_json
# Import pandas for data manipulation
import pandas as pd

# Import the path that the csv and json files are exported to with file_path
def test_export_csv_and_json(file_path):

    # test_data is created as a DataFrame with test data
    test_data = pd.DataFrame([{ "campaign": "Test", "impressions": 1000 }])

    # Get the file paths for the files using file_path
    csv_file = file_path / "output.csv"
    json_file = file_path / "output.json"

    # Call export_to_csv and export_to_json to test them
    export_to_csv(test_data, csv_file)
    export_to_json(test_data, json_file)

    # Test that the csv file is created after export_to_csv runs
    assert csv_file.exists()
    # Test that the json file is created after export_to_json runs
    assert json_file.exists()
    # Test that the csv file contains exported data
    assert csv_file.read_text().strip() != ""
    # Test that the json file contains a JSON array
    assert json_file.read_text().strip().startswith("[")
