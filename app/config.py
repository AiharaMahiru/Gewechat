from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # API Base URL
    API_BASE_URL: str = "http://0.0.0.0:2531/v2/api"
    
    # API Token
    API_TOKEN: str = ""
    
    # Connection settings
    TIMEOUT_SECONDS: int = 60
    
    # Application settings
    APP_NAME: str = "WeChatAPI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
settings = Settings()