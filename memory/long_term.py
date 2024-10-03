"""memgpt/memory/long_term.py

import json
import os
from memgpt.memory.persistence import save_memory_to_disk, load_memory_from_disk

class LongTermMemory:
    def __init__(self, storage_path):
        self.storage_path = storage_path
        self.memory_data = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.storage_path):
            return load_memory_from_disk(self.storage_path)
        return {}

    def save_memory(self):
        save_memory_to_disk(self.memory_data, self.storage_path)

    def add_memory(self, key, data):
        self.memory_data[key] = data
        self.save_memory()

    def get_memory(self, key):
        return self.memory_data.get(key, None)

    def delete_memory(self, key):
        if key in self.memory_data:
            del self.memory_data[key]
            self.save_memory()
"""