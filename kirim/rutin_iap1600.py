import argparse
import datetime
import subprocess,sys
import os
sys.path.insert(0,'..')
sys.path.insert(0,'.')

from mailer import Mailer
from mailer import Message
from mailconf import MAILER_CONF,IDENTITY,IAP1600_MAILLIST,REPORT_DEF_CC


parser = argparse.ArgumentParser()
parser.add_argument('--filename', help='filename')
args = parser.parse_args()

message = Message(From=IDENTITY['from'],
                  To=IAP1600_MAILLIST['to'],
                  CC=IAP1600_MAILLIST['cc']+REPORT_DEF_CC,
                  Subject="User Service - Rutin Harian - IAP1600")

message.Body = """
Yth. Bapak/Ibu,

Terlampir Report IAP1600.

Salam,
%s
""" % (IDENTITY['signature'])
# filename = args.filename or "IVR7050U.xls"
filename = args.filename
message.attach(os.path.join(os.path.expanduser('~'),"mfoutlist",filename))

sender = Mailer(**MAILER_CONF)
sender.send(message)