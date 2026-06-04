# Multi-Agent Supply Chain Operations Twin

An enterprise-grade agentic workflow utilizing LangGraph and Gemini 3.5 Flash to autonomously resolve supply chain disruptions. This system shifts anomaly resolution from manual ERP data aggregation to autonomous, deterministic graph execution.

## Architecture & State Machine

This application enforces structural determinism. Large Language Models are constrained to specific nodes to prevent hallucination, utilizing strict Pydantic schemas and programmatic validation loops.

## Project Structure

```
supply-chain-agent-twin/
├── README.md             # Documentation
├── main.py               # Application entry point
│
├── data/
│   └── inventory.json    # Mock enterprise database
│
└── src/
    ├── __init__.py
    ├── state.py          # LangGraph state definitions
    ├── agents.py         # Agent node definitions
    └── tools.py          # Deterministic Python functions
```

## Setup

1. Clone the repository and navigate to the project directory:
   ```bash
   cd supply-chain-agent-twin
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. Run the application:
   ```bash
   python main.py
   ```

## Features

- **LangGraph Agents**: Agentic workflows for supply chain optimization
- **Inventory Management**: Track and manage inventory levels
- **Order Processing**: Handle supply chain orders efficiently
- **Tool Integration**: Deterministic Python functions for core operations

## Requirements

- Python 3.9+
- LangGraph
- LangChain
- Additional dependencies listed in `requirements.txt`

