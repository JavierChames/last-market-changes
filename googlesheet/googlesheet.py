import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os, platform

if not(platform.system()== "Windows"):
    json_credentials = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'config/Googlesheet/market-changes-credentials.json'))
else:
    json_credentials = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'config\\Googlesheet\\market-changes-credentials.json'))


def googlesheetconnection():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_credentials, scope)
    gc = gspread.authorize(credentials)
    sh = gc.open("Market-changes")
    return sh
