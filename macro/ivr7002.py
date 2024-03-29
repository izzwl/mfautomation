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
parser.add_argument('--param', help='wip select')
parser.add_argument('--user', help='MPMCS32')
parser.add_argument('--output', help='output file name')
parser.add_argument('--runxls', help='run macro xls [y]')
parser.add_argument('--isrowbawah', help='[y/n]')

args = parser.parse_args()
isrowbawah = True if args.isrowbawah == 'y' else False

# default directory to keep outlist
OUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')

# outlist name
FILE        = os.path.join(OUTLIST_DIR,'IVR7002')

# jcl mainframe name
JCL         = "IMSVS.PROD.BMP.RUTIN(IVR7002)"

# tso user, must be logged off
TSO_USER    = args.user or "MPMCS32"

# sub name of outlist on sd.h ex. JOBXXX>DETAIL
# ex DETAIL = ['NON UMC']
DETAIL      = []

runxls = args.runxls or ''

# script instantiation
_mf_ibm     = X3270.X3270('mainframe','5000',TSO_USER,FILE,JCL,is_row_bawah=isrowbawah)
_mf_hrc     = X3270.X3270('hercules','6000',TSO_USER,FILE,JCL,is_row_bawah=isrowbawah)
# select to be used
try: 
    mf = { 'ibm':_mf_ibm,'hrc':_mf_hrc }.get( args.mf, _mf_ibm )
except:    
    mf = _mf_ibm

#calculate param for jcl
param       = "%s" % (args.param) if args.param else ''


#for movecursor to MPMCS99I section and set it
jcl_class   = { 'xy' : [5,10], 'val' : 'I', }
#for movecursor to user=MPMCS99 section
jcl_user    = { 'xy' : [7,26], }
#for movecursor to jcl parameter section
jcl_param   = { 'xy' : [18,8], 'val' : param }

# #run by passing these parameter
# mf = mf.handle(jcl_class, jcl_user, jcl_param, DETAIL)
args = [jcl_class, jcl_user, jcl_param, DETAIL]
mf.set_param(*args)
mf.handle()

if runxls.lower() == 'y':
    os.chdir('..')
    os.chdir('export')
    # sys.argv = [sys.argv[0],'--input='+FILE,'--output='+FILE]
    sys.argv = [sys.argv[0]]
    execfile(__file__)
