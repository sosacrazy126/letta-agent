"""memgpt/memory/short_term.py

class ShortTermMemory:
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.memory = []

    def add_memory(self, data):
        if len(self.memory) >= self.capacity:
            self.memory.pop(0)  # Remove the oldest memory
        self.memory.append(data)

    def get_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory = []
"""