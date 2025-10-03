"""
Application settings and configuration
"""
from functools import lru_cache # (함수 캐싱) 설정 인스턴스를 싱글톤으로 사용하기 위해
from pydantic_settings import BaseSettings # .env 환경변수 읽기
from pydantic import Field, computed_field # 필드 지정용


class Settings(BaseSettings):
    """Application settings"""
    
    # Application
    APP_NAME: str = Field(default="MME-BOT", description="Application name")
    VERSION: str = Field(default="1.0.0", description="Application version")
    DEBUG: bool = Field(default=True, description="Debug mode")
    
    # Server
    HOST: str = Field(default="127.0.0.1", description="Server host")
    PORT: int = Field(default=1234, description="Server port")
    
    # CORS
    ALLOWED_ORIGINS: list[str] = Field(
        default=["http://localhost:1234"],
        description="Allowed CORS origins"
    )

    # Database
    POSTGRES_USER: str = Field(..., description="DB user")
    POSTGRES_PASSWORD: str = Field(..., description="DB password")
    POSTGRES_HOST: str = Field(default="localhost", description="DB host")
    POSTGRES_PORT: int = Field(default=5432, description="DB port")
    POSTGRES_DB: str = Field(..., description="DB name")

    @computed_field(return_type=str)
    @property
    def DATABASE_URL(self) -> str:
        return (
            # ex) postgresql://$user:$pwd@$host:$port/$db
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # Security
    SECRET_KEY: str = Field(
        default="secret",
        description="Secret key for JWT tokens"
    )
    ALGORITHM: str = Field(default="Base64", description="JWT algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(
        default=30,
        description="Access token expiration time in minutes"
    )
    
    # API
    API_VERSION: str = Field(default="/api/v1", description="API version prefix")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()
