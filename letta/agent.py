import logging
import os
from letta.memory.long_term import LongTermMemory
from letta.memory.short_term import ShortTermMemory
from letta.utils.nlp_tools import NLPTools
from letta.models.text_model import TextModel

class LettaAgent:
    def __init__(self, config):
        self.config = config
        self.setup_logging()
        self.long_term_memory = LongTermMemory(config['memory']['long_term_storage_path'])
        self.short_term_memory = ShortTermMemory(capacity=config['memory']['short_term_capacity'])
        self.nlp_tools = NLPTools()
        self.text_model = TextModel()

    def setup_logging(self):
        log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, 'letta.log')
        
        logging.basicConfig(
            level=self.config['logging']['level'],
            filename=log_file,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def process_input(self, user_input):
        try:
            self.logger.info(f"Processing user input: {user_input}")
            processed_input = self.nlp_tools.process_text(user_input)
            context = self.retrieve_memory()
            response = self.text_model.generate_text(processed_input, context)
            self.short_term_memory.add_memory(response)
            self.long_term_memory.add_memory('conversation', {'user': user_input, 'agent': response})
            self.logger.info(f"Generated response: {response}")
            return response
        except Exception as e:
            self.logger.error(f"Error processing input: {str(e)}")
            return "I'm sorry, but I encountered an error while processing your input."

    def retrieve_memory(self):
        recent_conversations = self.long_term_memory.get_recent_conversations(5)
        context = "The following is a conversation with an AI assistant:\n\n"
        for conv in recent_conversations:
            context += f"Human: {conv['user']}\nAI: {conv['agent']}\n"
        return context