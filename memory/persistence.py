"""
# memgpt/memory/persistence.py

import json

def save_memory_to_disk(memory_data, file_path):
    with open(file_path, 'w') as file:
        json.dump(memory_data, file)

def load_memory_from_disk(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
"""