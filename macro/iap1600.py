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
parser.add_argument('--param', help='PD2000001 PD2099999 A')
parser.add_argument('--user', help='MPMCS32')
parser.add_argument('--output', help='output file name')
parser.add_argument('--runxls', help='runxls (y/n)')
parser.add_argument('--sendmail', help='kirim email')
args = parser.parse_args()

_param = args.param.replace(' ','_')
is_runxls = args.runxls and args.runxls.lower() == 'y'
sendmail = args.sendmail or ''

# default directory to keep outlist
OUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')

# outlist name
if is_runxls:
    FILE        = os.path.join(OUTLIST_DIR,'IAP1600-'+_param)
else:
    FILE        = os.path.join(OUTLIST_DIR,'IAP1600')


# jcl mainframe name
JCL         = "IMSVS.PROD.BMP(IAP1600)"

# tso user, must be logged off
TSO_USER    = args.user or "MPMCS32"

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
end         = datetime.datetime.now()

output_filename = ""
if not args.param:
    output_filename = "%s - IAP1600.xls" % (end.strftime("%Y.%m.%d"),)
else:
    output_filename = "%s - IAP1600-%s.xls" % (end.strftime("%Y.%m.%d"),_param)


#for movecursor to MPMCS99I section and set it
jcl_class   = { 'xy' : [5,10], 'val' : 'A', }
#for movecursor to user=MPMCS99 section
jcl_user    = { 'xy' : [7,26], }
#for movecursor to jcl parameter section
jcl_param   = { 'xy' : [18,8], 'val' : param }

# #run by passing these parameter
# mf = mf.handle(jcl_class, jcl_user, jcl_param, DETAIL)
args = [jcl_class, jcl_user, jcl_param, DETAIL]
mf.set_param(*args)
mf.handle()

if is_runxls:
    os.chdir('..')
    os.chdir('export')
    # sys.argv = [sys.argv[0],'--input='+FILE,'--output='+FILE]
    # sys.argv = [sys.argv[0]]
    if output_filename:
        sys.argv = [sys.argv[0],'--input=IAP1600-'+_param,'--output=%s'%(output_filename)]
    else:
        sys.argv = ['','--input=IAP1600-'+_param,'--output=IAP1600-'+_param+'.xls']
    execfile(__file__)

if sendmail.lower() == 'y':
    os.chdir('..')
    os.chdir('kirim')
    # sys.argv = [sys.argv[0],'--input='+FILE,'--output='+FILE]
    sys.argv = [sys.argv[0],'--filename=%s'%(output_filename)]
    execfile("rutin_iap1600.py")