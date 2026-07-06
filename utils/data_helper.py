import json

def data_convert(filepath):
    with open(filepath) as f:
        converted_data = json.load(f)
        return converted_data