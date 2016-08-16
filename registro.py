from __future__ import print_function
import httplib2
import os
import requests
import json
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'cliente.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'
NEXUDUS_EMAIL = "jccubero96@gmail.com"
NEXUDUS_PASSWORD = "Chispa34"

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1TIY0AUlwRlrxzovvYvXnVqsVpwYdMzYg_R1Eilz4fts'
    rangeName = 'A2:E'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values',[])
    rows=[]
    response = requests.get('https://cubero.spaces.nexudus.com/api/spaces/coworkers',auth=(NEXUDUS_EMAIL,NEXUDUS_PASSWORD))
    coworkers = response.json();
    coworkers = json.dumps(coworkers)
    coworkers = json.loads(coworkers)
    for coworker in coworkers['Records']:
        if coworker :
            rows.append({
                'values':[{
                    'userEnteredValue':{'stringValue': coworker['FullName']}
                },
                {
                    'userEnteredValue':{'stringValue': coworker['Email']}
                },
                {
                    'userEnteredValue':{'numberValue': 1}
                }]
            })


    peticion={
        'updateCells': {
        'start': {'sheetId': 0, 'rowIndex': 0, 'columnIndex': 0},
        'rows':rows,
        'fields': 'userEnteredValue,userEnteredFormat.backgroundColor'
    }

    }
    batchUpdateRequest = {'requests': peticion}
    service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetId,
                                        body=batchUpdateRequest).execute()


if __name__ == '__main__':
    main()
