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
data = [
'220055',
'220056',
'220057',
'220058',
'220059',
'220060',
'220061',
'540007',
'540008',
'540009',
'540014',
'540017',
'540019',
'540024',
'540025',
'540026',
'540027',
'540028',
'540029',
'540030',
'540031',
'540032',
'540033',
'540034',
'540035',
'540036',
'540037',
'540038',
'540039',
'540043',
'540051',
'540052',
'540053',
'540054',
'540056',
'540057',
'540059',
'540060',
'540061',
'540062',
'540063',
'540064',
'540065',
'540066',
'540067',
'540068',
'540069',
'540070',
'540071',
'850140',
'850265',
'850558',
'851132',
'870267',
'870350',
'871162',
'871387',
'871413',
'871414',
'871424',
'871454',
'871494',
'871516',
'871533',
'871539',
'871540',
'871570',
'871672',
'871694',
'871700',
'871745',
'871772',
'880499',
'890085',
'890136',
'890162',
'890166',
'890280',
'890289',
'890314',
'890319',
'890326',
'890351',
'900055',
'900100',
'900107',
'900128',
'900138',
'900143',
'900150',
'900238',
'900241',
'900244',
'900292',
'900304',
'920067',
'920437',
'920438',
'920646',
'940081',
'950133',
'960057',
'960262',
'999020',
'999021',
'999037',
'999040',
'999041',
'999042',
'999047',
'999052',
'999055',
'999057',
'999058',
'999063',
'999064',
'999068',
'999070',
'999072',
'999074',
'999078',
'999079',
'999087',
'999089',
'999090',
'999092',
'999093',
]
tgl_awal = datetime.date(2022,8,29)
tgl_akhir = datetime.date(2022,8,29)
dt_str = tgl_awal.strftime("%d%m%y")

for nik in data:
    mf.movecursor(4,11).string("%s"%(nik))\
        .movecursor(5,11).string("%s"%(dt_str)).enter()\
        .movecursor(10,11).string("  ")\
        .enter()
    print(dt_str)

# for nik in data:
#     while tgl_awal <= tgl_akhir:
#         dt_str = tgl_awal.strftime("%d%m%y")
#         # nik = dt[0]
#         # ct_baru = str(dt[1]).zfill(2)
#         mf.movecursor(4,11).string("%s"%(nik))\
#             .movecursor(5,11).string("%s"%(dt_str)).enter()\
#             .movecursor(10,11).string("  ")\
#             .enter()
#         print(dt_str)
#         tgl_awal += datetime.timedelta(days=1)

