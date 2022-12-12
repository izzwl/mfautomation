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
emps = [
    '120001','120002','120003','120005','120006','120007','120009','120010','120011','120012','120013','120016','120017','120019','130001','130002','130005','130007','130009','130010','130012','130013','140003','140006','150045','150046','150047','150050','150052','150053','150054','150055','150057','150059','150061','150063','150065','150066','150067','150069','160043','160044','160047','160049','160050','160060','170004','170005','170006','170007','170008','170009','170010','170011','170012','170015','170017','170023','170025','170030','170031','170033','170034','170035','170036','170037','170038','170039','170040','170041','170042','170043','170044','180002','180003','180004','180005','180023','180024','180025','180026','180027','180028','180029','180032','180034','180035','180036','180038','180043','180046','180047','180049','180050','180052','180053','180054','180056','180058','180059','180060','180063','190001','190002','190003','190004','190005','190006','190007','190010','190011','190012','190013','190014','190016','190017','190018','190019','190020','190022','190023','190026','190027','190028','190029','190030','200003','200011','200012','200013','200014','200015','200016','200017','200018','200019','200020','200021','200022','200023','200024','200025','200026','200027','200028','200029','200030','200031','200032','200033','200034','200035','200036','200037','200038','200039','200040','200041','200042','200044','200045','200046','200047','200048','540002','540007','540008','540009','540010','540011','540012','540013','540014','540017','540019','540022','540024','540025','540026','540027','540028','540029','540030','540031','540032','540033','540034','540035','540036','540037','540038','540039','540043','540046','540049','540050','833128','840014','850140','850265','850558','850860','850863','850864','850872','850876','850888','850894','850898','850903','851036','851132','851182','851189','851191','860610','870267','870284','870310','870334','870350','870485','870566','870591','871146','871147','871162','871175','871176','871214','871247','871387','871405','871413','871414','871424','871454','871491','871494','871516','871520','871533','871539','871540','871545','871546','871570','871672','871694','871700','871745','871772','880141','880499','890085','890136','890162','890166','890199','890280','890289','890305','890314','890319','890326','890331','890351','900055','900056','900088','900100','900103','900107','900128','900138','900143','900150','900238','900241','900244','900255','900292','900304','900315','910099','910241','920067','920377','920437','920438','920621','920646','930211','930888','940004','940081','950133','960057','960262','999020','999021','999037','999040','999041','999042','999046','999047','999052','999055','999057','999058','999063','999064','999068','999070','999071','999072','999074','999078','999079','999087','999089','999090','999091','999092','999093'
]
date = [
    '010122',
]
#emp - ct baru
data_baru = [
    ['190004',10],
    ['200040',10],
    ['540032',10],
    ['540027',10],
    ['540030',10],
    ['871745',10],
    ['540009',10],
    ['540035',10],
    ['190001',10],
    ['540033',10],
    ['540037',10],
    ['871539',10],
    ['960057',10],
    ['871700',10],
    ['540043',10],
    ['120019',10],
    ['200025',10],
    ['890319',10],
    ['120002',10],
    ['200028',10],
    ['200018',10],
    ['540026',10],
    ['900088',10],
    ['150066',10],
    ['180043',10],
    ['180049',10],
    ['200045',10],
    ['540031',10],
    ['871772',10],
    ['540012',10],
    ['180060',10],
    ['540029',10],
    ['190028',10],
    ['200015',10],
    ['170034',10],
    ['150062',10],
    ['150065',10],
    ['200030',10],
    ['540013',10],
    ['150061',10],
    ['999093',10],
    ['180053',10],
    ['200017',10],
    ['900100',10],
    ['540024',10],
    ['150059',10],
    ['150067',10],
    ['890085',10],
    ['150057',10],
    ['150064',10],
    ['190016',10],
    ['180036',10],
    ['200048',10],
    ['930211',10],
    ['170037',10],
    ['170032',10],
    ['150063',10],
    ['900138',10],
    ['160049',10],
    ['160060',10],
    ['170005',10],
    ['170007',10],
    ['999058',10],
    ['540010',10],
    ['871454',10],
    ['540034',10],
    ['540038',10],
    ['190026',10],
    ['200027',10],
    ['200033',10],
    ['210010',10],
    ['540028',10],
    ['170042',10],
    ['871672',10],
    ['871694',10],
    ['170035',10],
    ['180023',10],
    ['540036',10],
    ['540039',10],
    ['200003',10],
    ['190018',10],
    ['180024',10],
    ['999040',10],
    ['540019',10],
    ['180034',10],
    ['540011',10],
    ['200016',10],
    ['180038',10],
    ['180064',10],
    ['200035',10],
    ['540007',10],
]

#for e in emps:
#     for d in date:
#         mf.movecursor(2,11).string("d%s%s"%(e,d)).enter().sleep(5).enter()

for dt in data_baru:
    nik = dt[0]
    ct_baru = str(dt[1]).zfill(2)
    print(nik,ct_baru)
    mf.movecursor(3,9).string("%s"%(nik)).enter()\
        .movecursor(6,12).string("%s"%(ct_baru)).enter()

