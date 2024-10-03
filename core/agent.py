"""memgpt/core/agent.py

from memgpt.memory.long_term import LongTermMemory
from memgpt.memory.short_term import ShortTermMemory
from memgpt.core.nlp_tools import NLPTools
from memgpt.tools.models.text_model import TextModel

class Agent:
    def __init__(self, config):
        self.long_term_memory = LongTermMemory(config['memory']['long_term_storage_path'])
        self.short_term_memory = ShortTermMemory(capacity=config['memory']['short_term_capacity'])
        self.nlp_tools = NLPTools()
        self.text_model = TextModel()

    def process_input(self, user_input):
        # Process user input
        processed_input = self.nlp_tools.process_text(user_input)
        
        # Retrieve relevant memory
        context = self.retrieve_memory()

        # Generate response using the text model
        response = self.text_model.generate_text(processed_input, context)
        
        # Update short-term memory
        self.short_term_memory.add_memory({'input': user_input, 'response': response})
        
        return response

    def retrieve_memory(self):
        # Combine short-term and long-term memory for context
        short_term = self.short_term_memory.get_memory()
        long_term = self.long_term_memory.load_memory()
        context = {'short_term': short_term, 'long_term': long_term}
        return context

    def save_long_term_memory(self):
        self.long_term_memory.save_memory()
"""