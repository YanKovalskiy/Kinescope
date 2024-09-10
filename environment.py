import os
from dotenv import load_dotenv


class Environment:
    @staticmethod
    def get_environment_variable(var: str):
        load_dotenv()
        return os.getenv(var)
