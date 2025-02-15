import os

from dotenv import load_dotenv


load_dotenv()


def get_debug():
    """Возвращение дебага"""
    return True if os.getenv('DEBUG') == 'True' else False
