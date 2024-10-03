"""memgpt/interface/cli.py

import argparse
from memgpt.core.agent import Agent
import yaml

def load_config(config_path='config/settings.yaml'):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def main():
    parser = argparse.ArgumentParser(description='MemGPT Agent CLI')
    parser.add_argument('--input', type=str, help='Input text for the agent')
    args = parser.parse_args()

    config = load_config()
    agent = Agent(config)

    if args.input:
        response = agent.process_input(args.input)
        print(f'Agent Response: {response}')
    else:
        print('Please provide an input using the --input argument.')

if __name__ == '__main__':
    main()
"""