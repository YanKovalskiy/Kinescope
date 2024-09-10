import os
from dotenv import load_dotenv


class Environment:
    def __init__(self):
        load_dotenv()

    @staticmethod
    def get_environment_variable(var):
        return os.getenv(var)
