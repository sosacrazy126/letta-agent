import json
from collections import deque

class LongTermMemory:
    def __init__(self, storage_path):
        self.storage_path = storage_path
        self.memory = self.load_memory()
        self.conversation_history = deque(maxlen=100)  # Store last 100 conversations

    def load_memory(self):
        try:
            with open(self.storage_path, 'r') as file:
                data = json.load(file)
                self.conversation_history = deque(data.get('conversation_history', []), maxlen=100)
                return data
        except FileNotFoundError:
            return {'conversation_history': []}

    def save_memory(self):
        with open(self.storage_path, 'w') as file:
            self.memory['conversation_history'] = list(self.conversation_history)
            json.dump(self.memory, file)

    def add_memory(self, key, value):
        if key == 'conversation':
            self.conversation_history.append(value)
        self.memory[key] = value
        self.save_memory()

    def get_memory(self, key):
        return self.memory.get(key)

    def delete_memory(self, key):
        if key in self.memory:
            del self.memory[key]
            self.save_memory()

    def get_recent_conversations(self, n):
        return list(self.conversation_history)[-n:]