from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    supabase_url: str
    supabase_anon_key: str
    qdrant_url: str
    qdrant_api_key: str
    neo4j_uri: str
    neo4j_username: str
    neo4j_password: str
    openai_api_key: str | None = None

    class Config:
        env_file = ".env"   # tells Pydantic to load from .env

# create global settings instance
settings = Settings()
