import sys
import os
import argparse
import yaml
import logging
import traceback

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

print(f"Python version: {sys.version}")
print(f"Current working directory: {os.getcwd()}")
print(f"sys.path: {sys.path}")

try:
    from letta.agent import LettaAgent
    print("Successfully imported LettaAgent")
except ImportError as e:
    print(f"Error: Unable to import LettaAgent. Exception details: {e}")
    print("Traceback:")
    traceback.print_exc()
    sys.exit(1)

def load_config(config_path='config/settings.yaml'):
    """
    Load the configuration from the specified YAML file.
    """
    try:
        with open(os.path.join(current_dir, config_path), 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        logging.error(f"Error loading configuration: {str(e)}")
        return None

def interactive_mode(agent):
    """
    Run the Letta Agent in interactive mode, allowing for continuous conversation.
    """
    print("Entering interactive mode. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = agent.process_input(user_input)
        print(f"Letta: {response}")

def main():
    """
    Main function to run the Letta Agent CLI.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Letta Agent CLI')
    parser.add_argument('--input', type=str, help='Input text for the agent')
    parser.add_argument('--config', type=str, default='config/settings.yaml', help='Path to the configuration file')
    parser.add_argument('--interactive', action='store_true', help='Run in interactive mode')
    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)
    if not config:
        print("Failed to load configuration. Exiting.")
        return

    # Initialize the agent
    agent = LettaAgent(config)

    # Process user input or run in interactive mode
    if args.interactive:
        interactive_mode(agent)
    elif args.input:
        response = agent.process_input(args.input)
        print(f'Agent Response: {response}')
    else:
        print('Please provide an input using the --input argument or use --interactive for interactive mode.')

if __name__ == '__main__':
    main()