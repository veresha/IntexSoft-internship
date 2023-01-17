from pydantic import BaseSettings


class Settings(BaseSettings):
    db_user: str
    db_password: str
    host_address: str
    db_name: str
    env: str
    database: str
    rabbitmq_broker: str

    class Config:
        env_file = '.env'


settings = Settings()
