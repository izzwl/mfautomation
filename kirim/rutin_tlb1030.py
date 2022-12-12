import argparse
import datetime
import subprocess,sys
import os
sys.path.insert(0,'..')
sys.path.insert(0,'.')

from mailer import Mailer
from mailer import Message
from mailconf import MAILER_CONF,IDENTITY,TLB1030_MAILLIST,REPORT_DEF_CC


parser = argparse.ArgumentParser()
parser.add_argument('--filename', help='filename')
args = parser.parse_args()

message = Message(From=IDENTITY['from'],
                  To=TLB1030_MAILLIST['to'],
                  CC=TLB1030_MAILLIST['cc'] + REPORT_DEF_CC,
                  Subject="User Service - Rutin Pekanan - TLB1030")

message.Body = """
DH,

Terlampir Report Pekanan TLB1030.

Salam,
%s
""" % (IDENTITY['signature'])
# filename = args.filename or "TLB1030.xls"
filename = args.filename
message.attach(os.path.join(os.path.expanduser('~'),"mfoutlist",filename))

sender = Mailer(**MAILER_CONF)
sender.send(message)