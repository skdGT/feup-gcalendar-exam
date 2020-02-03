from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import feupy
import sys

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

COURSES_IDS = {
    "MIEIC"  : 742,
    "LCEEMG" : 738,
    "MIEC"   : 740,
    "MIEIG"  : 725,
    "MIEEC"  : 741,
    "MIEM"   : 743,
    "MIEMM"  : 744,
    "MIEQ"   : 745
}

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

    """
        TODO:
            - ADD OPTION TO MANUALLY ADD EXAMS
    """

    id = sys.argv[2].upper()

    course = feupy.Course(COURSES_IDS[id])
    exams = course.exams(use_cache=False)
    year = int(sys.argv[1])

    to_add = []

    print("Upcoming Exams")
    for exam in exams:
        uc = exam["curricular unit"]
        if uc.curricular_year == year:
            to_add.append(exam)
            if exam["rooms"] is not None:
                rooms = ", ".join(exam["rooms"])
            else:
                rooms = None
            name = exam["curricular unit"].acronym
            day = exam["start"].date()
            start = str(exam["start"].time())[:5]
            finish = str(exam["finish"].time())[:5]

            print(name, "\t", day, start, finish, rooms)

    for exam in to_add:
        if exam["rooms"] is not None:
            rooms = ", ".join(exam["rooms"])
        else:
            rooms = None

        if exam['season'][0] == 'R':
            rec = " - R"
        else:
            rec = ""

        event = {
            'summary': '🎓' + exam["curricular unit"].acronym + rec,
            'location': rooms,
            'start': {
                'dateTime': str(exam['start'].date()) + "T" + str(exam["start"].time())[:5] + ":00",
                'timeZone': 'Europe/Lisbon',
            },
            'end': {
                'dateTime': str(exam['finish'].date()) + "T" + str(exam["finish"].time())[:5] + ":00",
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
    A script to automatically add exam events to Google Calendar.
    
    Usage:
        python create_events.py <curricular year> <course acronym>
    
    Adds every next exam to the calendar with rooms and a 1 day reminder.
"""

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(main.__doc__)
        exit()

    main()
