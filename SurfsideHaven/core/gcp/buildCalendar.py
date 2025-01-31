from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
import google.auth

# Use a more standard environment variable name unless specific project needs differ
SERVICE_ACCOUNT_FILE = os.getenv("GCP_CALENDAR_CREDS")

# Scope modification depends on whether you need read-only or full access
SCOPES = ['https://www.googleapis.com/auth/calendar']  

if SERVICE_ACCOUNT_FILE:
    # Load credentials from the service account file
    credentials, project = google.auth.load_credentials_from_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Build the service object for the API
    service = build('calendar', 'v3', credentials=credentials)
else:
    print("Environment variable for Google credentials not set.")