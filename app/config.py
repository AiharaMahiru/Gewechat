from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
    # API Base URL
    API_BASE_URL: str = Field(default="http://服务ip:2531/v2/api")
    
    # API Token
    API_TOKEN: str = Field(default="")
    
    # Connection settings
    TIMEOUT_SECONDS: int = Field(default=60)
    
    # Application settings
    APP_NAME: str = Field(default="WeChatAPI")
    APP_VERSION: str = Field(default="1.0.0")
    DEBUG: bool = Field(default=False)
    
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8"
    }
        
settings = Settings()