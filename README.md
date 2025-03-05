# WeChat API Service

A FastAPI-based RESTful API service for WeChat operations. This project is a Python port of a Java-based WeChat API service, providing the same functionality with modern Python features.

## Project Overview

This API service allows for programmatic management of WeChat functionalities including:

- Sending and managing various message types (text, images, videos, files)
- Login and authentication
- Personal profile management
- Group chat operations
- Contact management
- Favorites management
- Content downloading

## Project Structure

```
app/
├── main.py                   # FastAPI application entry point
├── config.py                 # Configuration settings
├── utils/
│   ├── __init__.py
│   └── http_client.py        # HTTP client utility
├── api/
│   ├── __init__.py
│   ├── message.py            # Message operations API
│   ├── login.py              # Login operations API
│   ├── personal.py           # Personal profile operations API
│   ├── group.py              # Group operations API
│   ├── label.py              # Label operations API
│   ├── favor.py              # Favorites operations API
│   ├── download.py           # Download operations API
│   └── contact.py            # Contact operations API
└── routers/
    ├── __init__.py
    ├── message.py            # Message endpoints
    ├── login.py              # Login endpoints
    ├── personal.py           # Personal profile endpoints
    ├── group.py              # Group endpoints
    ├── label.py              # Label endpoints
    ├── favor.py              # Favor endpoints
    ├── download.py           # Download endpoints
    └── contact.py            # Contact endpoints
```

## Features

- **Asynchronous API**: Built with FastAPI's async support for high-performance API calls
- **Type Annotations**: Comprehensive type hints for better code quality and IDE support
- **Modular Design**: Well-organized code structure with clear separation of concerns
- **Interactive Documentation**: Automatic OpenAPI documentation with Swagger UI

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn (ASGI server)
- HTTPX (for async HTTP requests)
- Pydantic (for data validation)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/wechat-api.git
   cd wechat-api
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

4. Configure your environment:
   - Create a `.env` file in the project root
   - Add your configuration settings (see [Configuration](#configuration))

## Configuration

Create a `.env` file with the following settings:

```env
API_BASE_URL=http://服务ip:2531/v2/api
API_TOKEN=your_api_token
DEBUG=False
```

Alternatively, you can set these values as environment variables.

## Running the Service

Start the service with Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000, and the interactive documentation will be at http://localhost:8000/docs.

## API Documentation

Once the service is running, you can access the automatically generated interactive API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Usage Examples

### Sending a text message

```python
import httpx
import asyncio

async def send_message():
    data = {
        "app_id": "your_app_id",
        "to_wxid": "recipient_wxid",
        "content": "Hello, this is a test message",
        "ats": ""
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8000/api/message/send_text", json=data)
        return response.json()

# Run the async function
result = asyncio.run(send_message())
print(result)
```

### Logging in with QR code

```python
import httpx
import asyncio

async def login():
    data = {
        "app_id": ""  # Empty for first login
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8000/api/login/get_qr", json=data)
        return response.json()

# Run the async function
result = asyncio.run(login())
print(result)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

This project is a Python port of a Java-based WeChat API service, maintaining the same functionality while leveraging Python's modern features.
