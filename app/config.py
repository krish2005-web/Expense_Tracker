from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Local development can continue using PostgreSQL through .env.
    # If DATABASE_URL is not supplied (for example on a simple Render demo),
    # the app falls back to a local SQLite file.
    DATABASE_URL: str = "sqlite:///./expense_tracker.db"
    SECRET_KEY: str = "dev-only-change-this-in-production"
    ALGORITHM: str = "HS256"
    FRONTEND_URL: str = "http://localhost:5500"


settings = Settings()
