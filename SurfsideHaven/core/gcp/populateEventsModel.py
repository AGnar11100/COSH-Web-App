import os
import sys
import django

# Get the project root (where manage.py is located)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

# Add the `core` directory to sys.path to access models properly
core_path = os.path.join(project_root, "SurfsideHaven", "core")
sys.path.append(core_path)

# Debugging
# print("sys.path:", sys.path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SurfsideHaven.settings")
django.setup()

from core.models import Event
from core.gcp.buildCalendar import service
from datetime import datetime, timezone

def fetch_and_populate_events():
    now = datetime.now(timezone.utc).isoformat()
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    for event in events:
        start_dt = datetime.fromisoformat(event['start']['dateTime'].replace('Z', '+00:00'))
        end_dt = datetime.fromisoformat(event['end']['dateTime'].replace('Z', '+00:00'))

        Event.objects.update_or_create(
            title=event['summary'],
            location=event.get('location', 'No location provided'),
            description=event.get('description', ''),
            start_datetime=start_dt,
            end_datetime=end_dt,
        )

if __name__ == "__main__":
    fetch_and_populate_events()
