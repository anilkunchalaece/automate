
from __future__ import print_function
import httplib2
import os
import json

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'


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
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
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
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    #get the all unread messages
    results = service.users().messages().list(userId='me',labelIds=['UNREAD','CATEGORY_PERSONAL']).execute()

    messages = []
    emails = {}
    returnVal = []


    if 'messages' in results:
      messages.extend(results['messages'])

    print("Total Un-Read Messages are -> "+str(len(messages)))
    for message in messages :
        mId = messages[0]['id']
        msgPayload = service.users().messages().get(userId='me',id=mId).execute()
        for header in msgPayload['payload']['headers'] :
            #print(header)

            if header['name'] == "From" :
                #print(header['value'])
                emails['sender'] = header['value']

            if header['name'] == 'Subject':
                #print(header['value'])
                emails['subject'] = header['value']
        returnVal.append(emails)


    #print(senderList)
    #print(subjectList)
    return returnVal
if __name__ == '__main__':
    main()
