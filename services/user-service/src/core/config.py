from pydantic_settings import BaseSettings


# BaseSettings auto-populates fields from environment variables (case-insensitive match by name).
class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        # Fall back to this file when a variable isn't set in the process environment.
        env_file = ".env"


# Module-level singleton so all imports share one parsed config object.
settings = Settings()
