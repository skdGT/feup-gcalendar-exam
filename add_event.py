from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    uc = input("Curricular Unit (acronym): ")
    rec = input("Regular Season? (y/n): ")
    rooms = input("Rooms (separate with space): ")
    day = input("Day (YYYY-MM-DD): ")
    start = input("Start Time (HH:MM): ")
    end = input("End Time (HH:MM): ")

    summary = '🎓' + uc
    if rec.upper() == "N":
        summary += " - R"

    event = {
        'summary': summary,
        'location': ', '.join(rooms.split()),
        'start': {
            'dateTime': day + "T" + start + ":00",
            'timeZone': 'Europe/Lisbon',
        },
        'end': {
            'dateTime': day + "T" + end + ":00",
            'timeZone': 'Europe/Lisbon',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {
                    'method': 'popup',
                    'minutes': 60 * 24,
                },
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print("Event created: %s" % (event.get('summary')))


main.__doc__ = """
    A script to manually add exam event to Google Calendar.

    Usage:
        python add_event.py

    Adds an exam or test event to Google Calendar with a 1 day reminder.
"""

if __name__ == '__main__':
    main()
