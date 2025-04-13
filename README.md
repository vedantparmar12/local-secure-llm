# Ollama API with FastAPI

A simple API wrapper for Ollama's language models using FastAPI with API key authentication and credit system.

## Features

- Fast API to interact with locally running Ollama models
- API key authentication system
- Credit-based usage tracking
- Easy customization and extension

## Prerequisites

- Python 3.7+
- Ollama installed and running locally
- Required Python packages (see Installation)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/ollama-fastapi.git
cd ollama-fastapi
```

2. Install required dependencies:
```bash
pip install fastapi uvicorn ollama python-dotenv pydantic
```

3. Create a `.env` file in the project root:
```
API_KEY=your_secret_api_key_here
```

## Usage

### Starting the API server

Run the FastAPI server:
```bash
uvicorn main:app --reload
```

The server will start at http://127.0.0.1:8000

### API Endpoints

#### POST /generate

Generates a response using the specified Ollama model.

**Request:**
- Headers:
  - `x-api-key`: Your API key (required)
  - `Content-Type`: application/json
- Body:
  ```json
  {
    "prompt": "Your prompt text here"
  }
  ```

**Response:**
```json
{
  "response": "Generated response from the model"
}
```

### Testing the API

You can test the API using the provided `test-api.py` script:

```bash
python test-api.py
```

Or using curl:

```bash
curl -X POST "http://127.0.0.1:8000/generate" \
  -H "Content-Type: application/json" \
  -H "x-api-key: your_secret_api_key_here" \
  -d '{"prompt": "Tell me about Python"}'
```

## Customization

### Changing the Model

To use a different Ollama model, edit the `generate` function in `main.py`:

```python
response = ollama.chat(model="your_model_name", messages=[{"role": "user", "content": request.prompt}])
```

### Modifying the Credit System

The API key credit system is managed through the `API_KEY_CREDITS` dictionary in `main.py`. You can adjust the number of credits per key or add additional keys.

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
