import argparse
import datetime
import subprocess,sys
import os
sys.path.insert(0,'..')
import X3270

"""
Note:
to run this script well, tso must meet the following condition:
1. x3270 run on scripting mode
2. xdc default dataset to [tsouser].transfer

...continue

"""
parser = argparse.ArgumentParser()
parser.add_argument('--mf', help='mf instance')
parser.add_argument('--param', help='TANPA INPUT')
parser.add_argument('--output', help='output file name')
args = parser.parse_args()

# default directory to keep outlist
OUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')

# outlist name
FILE        = os.path.join(OUTLIST_DIR,'MCR2008')

# jcl mainframe name
JCL         = "IMSVS.PROD.BMP(MCR2008)"

# tso user, must be logged off
TSO_USER    = "MPMCS99"

# sub name of outlist on sd.h ex. JOBXXX>DETAIL
# ex DETAIL = ['NON UMC']
DETAIL      = []

# script instantiation
print(TSO_USER)
print(FILE)
print(JCL)
_mf_ibm     = X3270.X3270('mainframe','5000',TSO_USER,FILE,JCL)
_mf_hrc     = X3270.X3270('hercules','6000',TSO_USER,FILE,JCL)
# select to be used
try: 
    mf = { 'ibm':_mf_ibm,'hrc':_mf_hrc }.get( args.mf, _mf_ibm )
except:    
    mf = _mf_ibm

#calculate param for jcl
param       = "%s" % (args.param)


#for movecursor to MPMCS99I section and set it
jcl_class   = { 'xy' : [5,10], 'val' : 'p', }
#for movecursor to user=MPMCS99 or notify=MPMCS99 section
jcl_user    = { 'xy' : [7,24], }
#for movecursor to jcl parameter section
jcl_param   = { 'xy' : [20,8], 'val' : param, }
# #run by passing these parameter
# mf = mf.handle(jcl_class, jcl_user, jcl_param, DETAIL)
args = [jcl_class, jcl_user, jcl_param, DETAIL]
mf.set_param(*args)
mf.handle()
