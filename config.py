# config.py
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
API_KEY = os.getenv("GOOGLE_API_KEY")

# Authentication
# Option 1: Service Account Key File
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

assert PROJECT_ID, "PROJECT_ID not found in environment"
assert LOCATION, "LOCATION not found in environment"
assert API_KEY, "API_KEY not found in environment"
assert GOOGLE_APPLICATION_CREDENTIALS, "GOOGLE_APPLICATION_CREDENTIALS not found"
# Option 2: Set environment variables for ADC (Application Default Credentials)
# Run: gcloud auth application-default login

# Vertex AI Model Settings
IMAGEN_MODEL = "imagegeneration@006"
MAX_IMAGES = 4
DEFAULT_ASPECT_RATIO = "1:1"

# Storage Settings
STORAGE_BUCKET_NAME = f"{PROJECT_ID}-generated-images"
STORAGE_LOCATION = LOCATION

# Application Settings
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Marketing Agent Settings
MAX_CONTENT_LENGTH = 1000
DEFAULT_CAMPAIGN_TYPE = "AI tools and automation"

print(f"🔧 Config loaded - Project: {PROJECT_ID}, Location: {LOCATION}")