from dotenv import load_dotenv
import os

load_dotenv()

MODEL_ID = os.environ.get('MODEL_ID')
OPENAI_API = os.environ.get('OPENAI_API')
OPENAI_KEY = os.environ.get('OPENAI_KEY')