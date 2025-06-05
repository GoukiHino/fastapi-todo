import secrets
from typing import List, Optional


class Settings:
    PROJECT_NAME: str = "FastAPI Todo"
    API_PREFIX: str = "/api/v1"

    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24

    CORS_ORIGINS: List[str] = [
        "http://localhost", "https://localhost", "http://localhost:3000", "https://localhost:3000"
    ]

    DB_DIALECT: str = "sqlite"
    DB_HOST: Optional[str] = None
    DB_PORT: Optional[str] = None
    DATABASE: str = "app.db"
    DB_USERNAME: Optional[str] = None
    DB_PASSWORD: Optional[str] = None

    @property
    def DB_URI(self) -> str:
        uri = f"{self.DB_DIALECT}://"
        if self.DB_USERNAME and self.DB_PASSWORD:
            uri += f"{self.DB_PASSWORD}:{self.DB_PASSWORD}"
        if self.DB_HOST and self.DB_PORT:
            uri += f"@{self.DB_HOST}:{self.DB_PORT}"
        uri += f"/{self.DATABASE}"
        return uri


settings = Settings()
