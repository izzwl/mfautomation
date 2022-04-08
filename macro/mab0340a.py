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
parser.add_argument('--param', help='444555')
parser.add_argument('--cutoff', help='211231')
# parser.add_argument('--user', help='MPMCS32')
parser.add_argument('--output', help='output file name')
parser.add_argument('--runxls', help='run macro xls [y]')

args = parser.parse_args()

runxls = args.runxls or ''

# default directory to keep outlist
OUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')

# outlist name
FILE        = os.path.join(OUTLIST_DIR,'MAB0340A-'+args.param)

# jcl mainframe name
JCL         = "IMSVS.PROD.BMP(MAB0340A)"

# tso user, must be logged off
TSO_USER    = "MPMCS99"

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
jcl_class   = { 'xy' : [5,10], 'val' : 'M', }
#for movecursor to user=MPMCS99 section
jcl_user    = { 'xy' : [6,23], }
#for movecursor to jcl parameter section
jcl_param   = { 'xy' : [18,8], 'val' : param, 'scroll' : 1 }

param_cutoff = args.cutoff if args.cutoff else datetime.datetime.now().strftime("%y%m%d")

jcl_param_list   = [
    { 'xy' : [14,8], 'val' : param_cutoff },
    { 'xy' : [18,8], 'val' : param },
]

# #run by passing these parameter
# mf = mf.handle(jcl_class, jcl_user, jcl_param, DETAIL)
args = [jcl_class, jcl_user, jcl_param, DETAIL]
mf.set_param(*args)
mf.set_jcl_param_list(jcl_param_list)
mf.handle()

# if runxls.lower() == 'y':
os.chdir('..')
os.chdir('export')
# sys.argv = [sys.argv[0],'--input='+FILE,'--output='+FILE]
sys.argv = ['','--input=MAB0340A-'+param,'--output=MAB0340A-'+param+'.xls']
# sys.argv = [sys.argv[0]]
execfile(__file__)