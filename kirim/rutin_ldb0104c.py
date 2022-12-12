import argparse
import datetime
import subprocess,sys
import os
sys.path.insert(0,'..')
sys.path.insert(0,'.')

from mailer import Mailer
from mailer import Message
from mailconf import MAILER_CONF,IDENTITY,LDB0104C_MAILLIST,REPORT_DEF_CC


parser = argparse.ArgumentParser()
parser.add_argument('--filename', help='filename')
args = parser.parse_args()

message = Message(From=IDENTITY['from'],
                  To=LDB0104C_MAILLIST['to'],
                  CC=LDB0104C_MAILLIST['cc'] + REPORT_DEF_CC,
                  Subject="User Service - Rutin Pekanan - Utilisasi Man Hour")

message.Body = """
Yth. Bu Nani,

Terlampir Report Pekanan Utilisasi Man Hour.

Salam,
%s
""" % (IDENTITY['signature'])
# filename = args.filename or "LDB0104C.xls"
filename = args.filename
message.attach(os.path.join(os.path.expanduser('~'),"mfoutlist",filename))

sender = Mailer(**MAILER_CONF)
sender.send(message)