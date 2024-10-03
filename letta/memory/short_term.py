from collections import deque

class ShortTermMemory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = deque(maxlen=capacity)

    def add_memory(self, item):
        self.memory.append(item)

    def get_memory(self):
        return list(self.memory)

    def clear_memory(self):
        self.memory.clear()