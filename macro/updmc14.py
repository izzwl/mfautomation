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
parser.add_argument('--niktgl', help='150029010120')
parser.add_argument('--output', help='output file name')
args = parser.parse_args()

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
# data = ['170042','180027']
data = ['180027',]
tgl_awal = datetime.date(2021,8,2)
tgl_akhir = datetime.date(2021,8,27)
for nik in data:
    while tgl_awal <= tgl_akhir:
        dt_str = tgl_awal.strftime("%d%m%y")
        # nik = dt[0]
        # ct_baru = str(dt[1]).zfill(2)
        mf.movecursor(4,11).string("%s"%(nik))\
            .movecursor(5,11).string("%s"%(dt_str)).enter().enter()
        print(dt_str)
        tgl_awal += datetime.timedelta(days=1)

