from buildCalendar import service
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import os

# Google API client setup
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = os.getenv("GCP_CALENDAR_CREDS")

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# service = build('calendar', 'v3', credentials=credentials)

# Current date setup
start_date = datetime.now()

for i in range(20):
    # Create an event starting today and each subsequent day
    event_date = start_date + timedelta(days=i)
    start_time = event_date.strftime('%Y-%m-%dT09:00:00-07:00')
    end_time = event_date.strftime('%Y-%m-%dT10:00:00-07:00')

    event = {
        'summary': 'Team Meeting',
        'location': '800 Howard St., Surfside Haven, CA 99999',
        'description': 'Discuss project updates.',
        'start': {
            'dateTime': start_time,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'America/Los_Angeles',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    # Inserting the event into the calendar
    created_event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event created for {event_date.strftime('%Y-%m-%d')}: {created_event.get('htmlLink')}")
