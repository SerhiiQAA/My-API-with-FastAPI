import json

def load_data(file_path='data.json'):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_data(data, file_path='data.json'):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)
