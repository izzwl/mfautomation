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
# parser.add_argument('--param', help='444555')
parser.add_argument('--paramfile', help='textfiles of wip')
# parser.add_argument('--user', help='MPMCS32')
parser.add_argument('--output', help='output file name')
parser.add_argument('--runxls', help='run macro xls [y]')

args = parser.parse_args()

runxls = args.runxls or ''
if not args.paramfile:
    exit('param not set')
# default directory to keep outlist
OUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')

PARAM_FILE        = os.path.join(OUTLIST_DIR,args.paramfile)

# jcl mainframe name
JCL         = "IMSVS.PROD.BMP(MAB0340A)"

# tso user, must be logged off
TSO_USER    = "MPMCS99"

# sub name of outlist on sd.h ex. JOBXXX>DETAIL
# ex DETAIL = ['NON UMC']
DETAIL      = []

nf = open(os.path.join(OUTLIST_DIR,'mab0340abatch.log'), "w+") 
f = open(PARAM_FILE, "r")
s = 0
lines = f.readlines()

for i,l in enumerate(lines):
    # outlist name
    FILE = os.path.join(OUTLIST_DIR,'MAB0340A-'+l)
    _mf_ibm     = None
    _mf_hrc     = None
    nf.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
    try:
        # script instantiation
        _mf_ibm     = X3270.X3270('mainframe','5000',TSO_USER,FILE,JCL)
        _mf_hrc     = X3270.X3270('hercules','6000',TSO_USER,FILE,JCL)
        # select to be used
        try: 
            mf = { 'ibm':_mf_ibm,'hrc':_mf_hrc }.get( args.mf, _mf_ibm )
        except:    
            mf = _mf_ibm

        #for movecursor to MPMCS99I section and set it
        jcl_class   = { 'xy' : [5,10], 'val' : 'M', }
        #for movecursor to user=MPMCS99 section
        jcl_user    = { 'xy' : [6,23], }
        #for movecursor to jcl parameter section
        jcl_param   = { 'xy' : [18,8], 'val' : l, 'scroll' : 1 }

        jcl_param_list   = [
            { 'xy' : [14,8], 'val' : datetime.datetime.now().strftime("%y%m%d") },
            { 'xy' : [18,8], 'val' : l },
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
        sys.argv = ['','--input=MAB0340A-'+l,'--output=MAB0340A-'+l+'.xls']
        # sys.argv = [sys.argv[0]]
        execfile('mab0340a.py')
        nf.write(l+' success'+'\n')

    except Exception as e:
        nf.write(l+' FAILED'+'\n')
        nf.write(str(e)+'\n')
        mf.disconnect()
        mf.sleep(5)
        