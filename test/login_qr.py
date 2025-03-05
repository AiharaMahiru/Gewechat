import httpx
import asyncio

async def login():
    # Using the correct parameter name (appId instead of app_id)
    data = {
        "appId": ""  # Empty for first login
    }
    
    async with httpx.AsyncClient() as client:
        # Using the correct endpoint path based on your API implementation
        response = await client.post("http://0.0.0.0:2531/v2/api/login/getLoginQrCode", json=data)
        return response.json()

if __name__ == "__main__":
    # Run the async function
    result = asyncio.run(login())
    print(result)