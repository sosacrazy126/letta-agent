# Letta (formerly MemGPT) Project

Letta is an AI-powered conversational agent that uses advanced language models and memory management techniques to engage in human-like conversations.

## Features

- Text generation using GPT-2
- NLP tools for text processing
- Long-term and short-term memory management
- Configurable settings
- Interactive CLI mode

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/letta.git
   cd letta
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Single Input Mode

To get a single response from the agent:

```
python main.py --input "Your input text here"
```

### Interactive Mode

To start an interactive conversation with the agent:

```
python main.py --interactive
```

### Custom Configuration

To use a custom configuration file:

```
python main.py --config path/to/your/config.yaml --interactive
```

## Running Tests

To run the unit tests:

```
pytest
```

## Project Structure

```
memgpt/
├── config/
│   └── settings.yaml
├── letta/
│   ├── models/
│   │   └── text_model.py
│   ├── utils/
│   │   └── nlp_tools.py
│   ├── memory/
│   │   ├── long_term.py
│   │   └── short_term.py
│   └── agent.py
├── tests/
│   └── test_agent.py
├── main.py
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.