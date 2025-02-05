from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.cloud import storage
import os
import google.auth
import json
from base64 import b64decode


# Use a more standard environment variable name unless specific project needs differ
# SERVICE_ACCOUNT_FILE = os.getenv("GCP_CALENDAR_CREDS") # For Development
ENCODED_KEY = os.getenv("COSH_GCP_SAJSON_HERO")
decoded_key = b64decode(ENCODED_KEY)
service_account_info = json.loads(decoded_key)

# Scope modification depends on whether you need read-only or full access
SCOPES = ['https://www.googleapis.com/auth/calendar']  

if service_account_info:
    # Load credentials from the service account file
    credentials, project = google.auth.load_credentials_from_file(service_account_info, scopes=SCOPES)

    # Build the service object for the API
    service = build('calendar', 'v3', credentials=credentials)
else:
    print("Environment variable for Google credentials not set.")