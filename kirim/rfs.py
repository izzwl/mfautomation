import argparse
import datetime
import subprocess,sys
import os
sys.path.insert(0,'..')
sys.path.insert(0,'.')

from mailer import Mailer
from mailer import Message
from mailconf import MAILER_CONF,IDENTITY,RFS_DEF_CC


parser = argparse.ArgumentParser()
parser.add_argument('--to', help='miftah@umcntp.co.id')
parser.add_argument('--yth', help='Pak Miftah')
parser.add_argument('--filename', help='filename')
parser.add_argument('--rfsno', help='2200399')
parser.add_argument('--remark', help='PPB1300A')
args = parser.parse_args()

subject = "RFS Number : %s (%s)"%(args.rfsno,args.remark)
message = Message(From=IDENTITY['from'],
                  To=args.to,
                  CC=RFS_DEF_CC,
                  Subject=subject)

message.Body = """
Yth. ,

Terlampir Report yang direquest melalui %s.

Salam,
%s
""" % (IDENTITY['signature'],subject)


filename = args.filename
message.attach(os.path.join(os.path.expanduser('~'),"mfoutlist",filename))

sender = Mailer(**MAILER_CONF)
sender.send(message)