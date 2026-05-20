import os
from dotenv import load_dotenv
from entsoe_e_pipeline.exceptions import ConfigError

load_dotenv()


class Config:
    required_vars = [
        "API_KEY",
        "BASE_URL",
        "AWS_ACCESS_KEY_ID",
        "AWS_SECRET_ACCESS_KEY",
        "AWS_BUCKET_NAME",
        "AWS_REGION",
        "PREFIX",
    ]

    @classmethod
    def get(cls, var_name):
        value = os.getenv(var_name)
        if value is None:
            raise ConfigError(f"Environment variable '{var_name}' is not set.")
        return value

    @classmethod
    def validate(cls):
        for var in cls.required_vars:
            cls.get(var)
