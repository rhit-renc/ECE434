#!/usr/bin/env python3

# Based on: https://github.com/googleworkspace/python-samples/tree/main/sheets/quickstart

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import time, sys

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1GSA4805MK-H0aieQ1GmOMr9Q62gqeACgWguzbKkXi1Q"
SAMPLE_RANGE_NAME = "A2"

mainDir = "/sys/class/hwmon/"
dev0 = "hwmon0/temp1_input"
dev1 = "hwmon1/temp1_input"
dev2 = "hwmon2/temp1_input"

temp0 = open(mainDir + dev0, "r").read()
temp1 = open(mainDir + dev1, "r").read()
temp2 = open(mainDir + dev2, "r").read()

def main():
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      # print(repr(vars(flow)))
      # creds = flow.run_local_server(open_browser=False)
      creds = flow.run_console()
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    # values = [ [time.time()/60/60/24+ 25569 - 4/24, sys.argv[1], sys.argv[2]]]
    while True:
        temp0 = open(mainDir + dev0, "r").read()
        temp1 = open(mainDir + dev1, "r").read()
        temp2 = open(mainDir + dev2, "r").read()
        values = [ [time.time()/60/60/24+ 25569 - 4/24, temp0, temp1, temp2]]
        body = {'values': values}
        result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME,
                                    valueInputOption='USER_ENTERED', 
                                    body=body
                                    ).execute()
        print(result)
        time.sleep(5)

  except HttpError as err:
    print(err)

if __name__ == "__main__":
  main()
