import json

def load_json(file_path):
    "Open json file and returns dict"
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data