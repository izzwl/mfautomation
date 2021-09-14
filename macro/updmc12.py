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
    '010121',
]
#emp - ct baru
data_baru = [
    ['120011',5],
    ['120012',5],
    ['160050',4],
    ['190004',8],
    ['900241',11],
    ['999064',1],
    ['120013',1],
    ['200040',10],
    ['540032',11],
    ['130010',6],
    ['540027',11],
    ['540030',11],
    ['871424',6],
    ['871520',10],
    ['871745',11],
    ['999070',2],
    ['180029',9],
    ['180035',11],
    ['190014',3],
    ['540009',10],
    ['850558',3],
    ['890280',5],
    ['920067',4],
    ['540035',11],
    ['130001',5],
    ['170008',6],
    ['170030',10],
    ['190001',6],
    ['180025',10],
    ['540033',11],
    ['540037',11],
    ['871539',7],
    ['960057',8],
    ['871516',4],
    ['871700',9],
    ['170023',10],
    ['540043',10],
    ['120003',11],
    ['200034',4],
    ['851036',8],
    ['900244',11],
    ['120019',11],
    ['920437',1],
    ['200025',8],
    ['890319',10],
    ['950133',5],
    ['120002',9],
    ['200031',6],
    ['170010',10],
    ['200028',9],
    ['871147',1],
    ['900315',2],
    ['999052',1],
    ['200018',10],
    ['540026',11],
    ['130012',2],
    ['200046',7],
    ['900103',1],
    ['210007',1],
    ['890314',1],
    ['900304',4],
    ['999020',2],
    ['190007',4],
    ['170009',5],
    ['850894',9],
    ['900088',8],
    ['150069',9],
    ['190022',7],
    ['150066',9],
    ['870334',11],
    ['960262',2],
    ['999021',1],
    ['180043',10],
    ['871570',1],
    ['210009',5],
    ['150053',1],
    ['180049',11],
    ['190006',7],
    ['120001',1],
    ['150050',7],
    ['180003',9],
    ['180058',1],
    ['850876',2],
    ['850872',1],
    ['999079',1],
    ['200010',7],
    ['200045',9],
    ['540031',11],
    ['890326',4],
    ['999074',7],
    ['180054',5],
    ['871772',9],
    ['900238',8],
    ['190023',3],
    ['540012',11],
    ['900292',10],
    ['850898',8],
    ['870566',11],
    ['999047',6],
    ['170040',2],
    ['850265',1],
    ['851189',11],
    ['870267',8],
    ['170041',6],
    ['540002',11],
    ['170015',7],
    ['180060',11],
    ['999089',6],
    ['540029',11],
    ['999041',1],
    ['120007',3],
    ['180002',6],
    ['180004',9],
    ['890305',1],
    ['170033',5],
    ['850140',2],
    ['850864',4],
    ['190013',7],
    ['190028',10],
    ['200015',8],
    ['540025',11],
    ['170034',11],
    ['170036',1],
    ['180027',3],
    ['850863',11],
    ['150062',9],
    ['150065',11],
    ['200030',9],
    ['540013',9],
    ['920377',1],
    ['150061',10],
    ['160043',6],
    ['999093',9],
    ['210002',6],
    ['130005',1],
    ['160044',9],
    ['180053',10],
    ['200017',8],
    ['890136',1],
    ['900100',5],
    ['200032',6],
    ['540024',11],
    ['200022',8],
    ['999090',8],
    ['150059',10],
    ['180006',8],
    ['890166',2],
    ['150067',11],
    ['540022',10],
    ['871540',4],
    ['180059',8],
    ['190030',6],
    ['210006',1],
    ['120005',11],
    ['120010',4],
    ['880499',1],
    ['890085',6],
    ['890351',3],
    ['999057',4],
    ['150057',10],
    ['150064',10],
    ['130007',3],
    ['190016',11],
    ['180036',11],
    ['200023',7],
    ['871387',1],
    ['920438',1],
    ['200048',8],
    ['930211',10],
    ['170037',11],
    ['540014',7],
    ['900128',1],
    ['870485',2],
    ['170032',10],
    ['150063',11],
    ['900087',1],
    ['920646',1],
    ['170025',9],
    ['871247',11],
    ['871414',2],
    ['900138',10],
    ['900143',2],
    ['190017',9],
    ['851132',7],
    ['900150',1],
    ['930888',4],
    ['999068',2],
    ['160049',1],
    ['200041',5],
    ['180005',8],
    ['850903',11],
    ['860610',1],
    ['871494',8],
    ['200047',7],
    ['870591',11],
    ['900055',7],
    ['190012',11],
    ['910241',11],
    ['999072',1],
    ['170044',9],
    ['999037',1],
    ['120016',7],
    ['160060',11],
    ['170038',9],
    ['210012',1],
    ['120009',6],
    ['170005',11],
    ['170007',10],
    ['890199',7],
    ['130009',5],
    ['130013',8],
    ['170004',5],
    ['999063',2],
    ['120017',3],
    ['170031',2],
    ['999092',6],
    ['200029',8],
    ['999078',10],
    ['190002',9],
    ['833128',6],
    ['871162',1],
    ['170006',11],
    ['871176',1],
    ['940081',6],
    ['999058',7],
    ['150029',6],
    ['190019',9],
    ['540010',11],
    ['871454',10],
    ['180026',7],
    ['540034',11],
    ['540038',11],
    ['871405',10],
    ['900056',11],
    ['540008',5],
    ['190026',1],
    ['200026',6],
    ['200027',9],
    ['920621',2],
    ['999046',6],
    ['200033',8],
    ['871146',1],
    ['200011',7],
    ['210010',11],
    ['540028',11],
    ['870350',9],
    ['150052',1],
    ['890162',4],
    ['170042',11],
    ['871672',11],
    ['871694',11],
    ['130002',2],
    ['170012',6],
    ['180028',4],
    ['200019',5],
    ['999071',1],
    ['160047',7],
    ['170035',11],
    ['180023',11],
    ['150047',7],
    ['540036',11],
    ['150055',10],
    ['180047',6],
    ['200044',5],
    ['200039',4],
    ['540017',5],
    ['890289',3],
    ['150045',1],
    ['200020',8],
    ['540039',11],
    ['170011',10],
    ['170039',8],
    ['200003',11],
    ['210008',1],
    ['871533',1],
    ['140006',11],
    ['150046',4],
    ['150054',1],
    ['190018',11],
    ['200014',8],
    ['180024',10],
    ['180050',6],
    ['200024',9],
    ['999040',8],
    ['540019',11],
    ['900107',1],
    ['170043',9],
    ['180034',10],
    ['180046',7],
    ['540011',11],
    ['180052',3],
    ['190005',11],
    ['200016',9],
    ['210011',1],
    ['999087',1],
    ['180038',8],
    ['180064',10],
    ['999055',8],
    ['190020',4],
    ['200021',6],
    ['871413',1],
    ['120006',8],
    ['200035',3],
    ['871214',1],
    ['999042',2],
    ['540007',11],
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

