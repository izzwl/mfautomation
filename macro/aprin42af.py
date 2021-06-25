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
parser.add_argument('--fileparam', help='file parameter status 2 must be at ~/mfoutlist')
args = parser.parse_args()

MFOUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')
# contoh format data
# 4921
# 6187
# 4996
# 6317
# 6317
# 6318
# 6318
# 6318
param = 'GPR-STS2'
try:
    param = args.fileparam or 'GPR-STS2'
except:
    pass

# script instantiation
_mf_ibm     = X3270.X3270('mainframe','5000')
_mf_hrc     = X3270.X3270('hercules','6000')
# select to be used
try: 
    mf = { 'ibm':_mf_ibm,'hrc':_mf_hrc }.get( args.mf, _mf_hrc )
except:    
    mf = _mf_ibm

#param param
# user       = "%s" % (args.user or '7374032mcsmis')

# mf.movecursor(0,68).string(user).enter()
# mf.sleep(2)

f = open(os.path.join(MFOUTLIST_DIR,param), "r")
lines = f.readlines()

data = list(dict.fromkeys(lines))
for d in data:
    _d = "%s"%(d.strip().ljust(4,' '))
    print(_d)
    mf.movecursor(2,8).string("I").movecursor(3,8)
    mf.string(_d).enter().sleep(3)
    mf.movecursor(2,8).string("R").enter().enter().sleep(3)
