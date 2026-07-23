from typing import Optional

from pydantic import BaseSettings


class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = "dev"
    
    class Config:
        env_file = ".env"
    
class GlobalConfig(BaseConfig):
    Database_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False
    
class DevConfig(GlobalConfig):
    class config:
        env_prefix: str = "DEV_"

class TestConfig(GlobalConfig):
    DATABASE_URL = "sqlite:///./test.db"
    DB_FORCE_ROLL_BACK = True
    
    class config:
        env_prefix: str = "TEST_"

class ProdConfig(GlobalConfig):
    class config:
        env_prefix: str = "PROD_"
        
def get_config(env_state: str):
    configs = {"dev": DevConfig, "prod": ProdConfig, "test": TestConfig}
    return configs[env_state]()
    
config = get_config(BaseConfig().ENV_STATE)