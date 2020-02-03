from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import sys

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

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    if len(sys.argv) == 2:
        max = sys.argv[1] + "T23:59:59Z"
        print('Getting the upcoming exams ...')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                          singleEvents=True, timeMax=max,
                                          orderBy='startTime').execute()
        events = events_result.get('items', [])
    else:
        print('Getting the upcoming exams ...')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        if event['summary'][0] == '🎓':
            service.events().delete(calendarId='primary', eventId=event['id']).execute()
            print("Event removed: %s" %  event['summary'])


main.__doc__ = """
    A python script to remove every exam or test
    
    Usage:
    
        python remove_events.py
            removes every upcoming exam or test event starting with a graduation hat.
            
        python remove_events.py <date>
            date - YYYY-MM-DD max date to remove exams starting with a graduation hat.
            removes every upcoming exam or test event up to a max date
"""


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print(main.__doc__)
        exit()

    main()
