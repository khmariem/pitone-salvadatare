#!/usr/bin/python3.5
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def create(parsed_user_input):
    '''
    This function takes a dictionary containing the details of the event that was generated from
    the user's input.
    It then takes care of creating the event on Google Calendar.
    '''

    #Taken from the google's Quickstart.py template
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
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    print(os.path.abspath('token.pickle'))

    service = build('calendar', 'v3', credentials=creds)

    print('Creating the event.....')
    event = service.events().insert(calendarId='primary', body=parsed_user_input).execute()
    print("Event created at: %s" % (event.get('htmllink')))


