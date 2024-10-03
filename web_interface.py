from flask import Flask, render_template, request, jsonify
from letta.agent import LettaAgent
import yaml

app = Flask(__name__)

def load_config(config_path='config/settings.yaml'):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

config = load_config()
agent = LettaAgent(config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = agent.process_input(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)