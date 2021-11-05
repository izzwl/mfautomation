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
parser.add_argument('--param', help='201001 201031')
parser.add_argument('--user', help='MPMCS99')
parser.add_argument('--runxls', help='runxls')
parser.add_argument('--output', help='output file name')
args = parser.parse_args()

# default directory to keep outlist
OUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')

_param = args.param.replace(' ','_')
is_runxls = args.runxls and args.runxls.lower() == 'y'
# outlist name
if is_runxls:
    FILE        = os.path.join(OUTLIST_DIR,'VRP1500-'+_param)
else:
    FILE        = os.path.join(OUTLIST_DIR,'VRP1500')

# jcl mainframe name
JCL         = "IMSVS.PROD.BMP(VRP1500)"

# tso user, must be logged off
TSO_USER    = args.user or "MPMCS99"

# sub name of outlist on sd.h ex. JOBXXX>DETAIL
# ex DETAIL = ['NON UMC']
DETAIL      = []

# script instantiation
_mf_ibm     = X3270.X3270('mainframe','5000',TSO_USER,FILE,JCL)
_mf_hrc     = X3270.X3270('hercules','6000',TSO_USER,FILE,JCL)
# select to be used
try: 
    mf = { 'ibm':_mf_ibm,'hrc':_mf_hrc }.get( args.mf, _mf_ibm )
except:    
    mf = _mf_ibm


#calculate param for jcl
param       = "%s" % (args.param) if args.param else ''


#for movecursor to MPMCS99I section and set it
jcl_class   = { 'xy' : [5,10], 'val' : 'V', }
#for movecursor to user=MPMCS99 section
jcl_user    = { 'xy' : [6,60], }
#for movecursor to jcl parameter section
jcl_param   = { 'xy' : [5,8], 'val' : param, 'scroll' : 1 }

# #run by passing these parameter
# mf = mf.handle(jcl_class, jcl_user, jcl_param, DETAIL)
args = [jcl_class, jcl_user, jcl_param, DETAIL]
mf.set_param(*args)
mf.handle()

if is_runxls:
    os.chdir('..')
    os.chdir('export')
    # sys.argv = [sys.argv[0],'--input='+FILE,'--output='+FILE]
    sys.argv = ['','--input=VRP1500-'+_param,'--output=VRP1500-'+_param+'.xls']
    # sys.argv = [sys.argv[0]]
    execfile(__file__)