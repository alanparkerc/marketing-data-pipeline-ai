import json

def export_to_csv(clean_data, filepath):
    clean_data.to_csv(filepath, index=False)

def export_to_json(clean_data, filepath):
    with open(filepath, "w") as f:
        json.dump(clean_data.to_dict(orient="records"), f, indent=2)
