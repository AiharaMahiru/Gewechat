import httpx
import asyncio

async def login():
    data = {
        "app_id": ""  # Empty for first login
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post("http://0.0.0.0:2531/v2/api/login/get_qr", json=data)
        return response.json()

# Run the async function
result = asyncio.run(login())
print(result)