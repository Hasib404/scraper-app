from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL = "mongodb://admin:password123@db:27017"
    MONGO_INITDB_DATABASE = "test"

    class Config:
        env_file = "./.env"


settings = Settings()
