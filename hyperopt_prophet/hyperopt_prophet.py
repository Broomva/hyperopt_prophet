from pydantic import BaseSettings, validator


def init():
    print("Hyperopt Prophet Utility Installed")


class HyperoptProphetSession(BaseSettings):
    ...

    class Config:
        env_file = ".env"
