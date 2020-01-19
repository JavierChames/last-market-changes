import json
import yagmail
import os
from  googlesheet  import googlesheet as retrievegs


def send_mail(days):
  this_folder = os.path.dirname(os.path.abspath(__file__))
  my_file = os.path.join(this_folder, "gmailcred.txt")

  cred_gmail=my_file
  credentials=[]
  f = open(cred_gmail, "r")
  for x in f:
    credentials.append(x.split('\n')[0])
  f.close()

  sh=retrievegs.googlesheetconnection()
  sheet = sh.worksheet("emailto")
  emailto = sheet.col_values(1)

  sender_email = credentials[0]
  subject = "Weekly report marketing changes in the last " + str(days) + " days"
  sender_password = credentials[1]
  yag = yagmail.SMTP(user=sender_email, password=sender_password)

  contents = [
    "Hello,",
    "Attached report of marketing changes in the last " + str(days) + " days"
  ]
  my_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'html/index.html'))

  yag.send(emailto, subject, contents, attachments=my_file)


