import httpx
import asyncio
import socket

async def test_connection():
    # Test if the port is open
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('0.0.0.0', 2531))
        print("✅ Connection to port 2531 successful")
        s.close()
    except Exception as e:
        print(f"❌ Connection to port 2531 failed: {e}")
        print("Make sure the WeChat API service is running on this port")
        return False
    
    # Test a simple GET request to see if the server responds
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://0.0.0.0:2531/")
            print(f"✅ HTTP GET request successful: {response.status_code}")
            print(f"Response: {response.text[:100]}...")
    except Exception as e:
        print(f"❌ HTTP GET request failed: {e}")
        print("The server might be running but not responding to HTTP requests")
    
    # Test the specific endpoint with proper error handling
    try:
        data = {"appId": ""}
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://0.0.0.0:2531/v2/api/login/getLoginQrCode", 
                json=data,
                timeout=10.0  # Increase timeout
            )
            print(f"✅ API endpoint request successful: {response.status_code}")
            print(f"Response: {response.text[:100]}...")
    except Exception as e:
        print(f"❌ API endpoint request failed: {e}")
        print("The specific endpoint might not be available or correctly implemented")

if __name__ == "__main__":
    asyncio.run(test_connection())