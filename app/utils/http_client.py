import json
import ssl
import httpx
from typing import Dict, Any, Optional

class HttpClient:
    base_url = "http://0.0.0.0:2531/v2/api"
    token = "123456"
    
    @staticmethod
    def create_ssl_context():
        """Create SSL context with verification disabled (equivalent to trust_all_certs in Java)"""
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        return ssl_context
    
    @classmethod
    async def post_json(cls, route: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Equivalent to postJSON in Java OkhttpUtil
        """
        headers = {}
        if cls.token:
            headers["X-GEWE-TOKEN"] = cls.token
        
        # Add content type header
        headers["Content-Type"] = "application/json"
        
        if not cls.base_url:
            raise RuntimeError("baseUrl not configured")
        
        url = f"{cls.base_url}{route}"
        
        try:
            # Create httpx client with SSL context and timeout
            async with httpx.AsyncClient(
                verify=False,  # Equivalent to TrustManager in Java
                timeout=60.0,  # Timeout in seconds
            ) as client:
                response = await client.post(
                    url, 
                    headers=headers,
                    json=params
                )
                
                # Log response for debugging
                print(response.text)
                
                # Parse response
                result = response.json()
                
                if result.get("ret") == 200:
                    return result
                else:
                    raise RuntimeError(response.text)
                    
        except Exception as e:
            print(f"url={url}")
            raise RuntimeError(str(e))