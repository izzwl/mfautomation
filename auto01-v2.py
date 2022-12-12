import datetime
import subprocess
import os,sys
from time import strftime

# hari = {
#     0 : 'minggu',
#     1 : 'senin',
#     2 : 'selasa',
#     3 : 'rabu',
#     4 : 'kamis',
#     5 : 'jumat',
#     6 : 'sabtu',
# }
# programs = [
#     'bcinbc23.py',
#     'bcmr02.py',
#     'bcin72.py',
#     'bcoutbc25.py',
#     'womaktif.py',
#     'bcinbc40.py',
#     'bcioutbc3.py',
# ]
program_hari = {
    'bcinbc23.py'   : [1,2,3,4,5],
    'bcmr02.py'     : [1,2,3,4,5],
    'bcin72.py'     : [1,2,3,4,5],
    'bcoutbc25.py'  : [1,2,3,4,5],
    'womaktif.py'   : [1,2,3,4,5],
    'bcinbc40.py'   : [1,2,3,4,5],
    'bcoutbc3.py'   : [1,2,3,4,5],
    'ivr7050m.py'   : [5], #<-ini bagian accounting
}
program_accounting_plus = [
    'iap1300k.py','iap1300b.py','iap1400k.py','iap1400b.py','iap1700.py','vrp1200.py',
]
program_jenis = {
    'bcinbc23.py'   : 'BCINBC23',
    'bcmr02.py'     : 'BCMR02',
    'bcin72.py'     : 'BCIN72',
    'bcoutbc25.py'  : 'BCOUTBC25',
    'womaktif.py'   : 'WOMAKTIF',
    'bcinbc40.py'   : 'BCINBC40',
    'bcoutbc3.py'   : 'BCOUTBC3',
    'ivr7050m.py'   : '',
}
mf = ''
autos = ['bc','accounting',]
param_tanggal = ''
try :
    mf = sys.argv[1]
except:
    pass

try :
    param_tanggal = sys.argv[3]
except:
    pass

try:
    auto = sys.argv[2]   
except:
    auto = ''
if auto == 'all':
    autos = autos
elif auto in autos:
    autos = [auto,]
else:
    exit('arg 2, harus ada autos all,bc,accouting')

mfuser = 'MPMCS99' if mf == 'hrc' else 'MPMCS32'
macro_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'macro',)
uploader_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'uploader',)
# print(macro_dir)
message = []
now = datetime.datetime.now()
hmin7 = now - datetime.timedelta(days=-7) 
ew  = now.strftime("%w") 
param_hmin7 = param_tanggal or "%s %s"%(hmin7.strftime("%y%m%d"),now.strftime("%y%m%d"))
param_bm = "BM%s00000 BM%s99999"%(now.strftime("%y"),now.strftime("%y"))
param_inv = "%s I I"%param_hmin7



for auto in autos:
    if auto == 'bc':
        for program,hari in program_hari.items():
            try:
                if int(ew) in hari:
                    proses = [
                        ['python', "%s"%(os.path.join(macro_dir,program)), mf,]
                    ]
                    if program_jenis[program]:
                        proses.append(['python', "%s"%(os.path.join(uploader_dir,'bcupload.py')),"--jenis=%s"%(program_jenis[program])])
                    for i,x in enumerate(proses):
                        subprocess.call(x)
                        print("Finished: "+str(i)+" "+ program)
                    message.append("Finished: %s at %s" % (
                        program,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    ))
                else:
                    print("Not scheduled:" + program)
                    message.append("Not scheduled: %s at %s" % (
                        program,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    ))
            except Exception as e:
                print("Error:" + program)
                message.append("Error: %s at %s" % (
                    program,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ))
                message.append("Exception: %s" % e ) 
    elif auto == 'accounting':
        param_dicts = {
            'iap1300k.py':param_hmin7,
            'iap1300b.py':param_hmin7,
            'iap1400k.py':param_hmin7,
            'iap1400b.py':param_hmin7,
            'iap1700.py':param_bm,
            'vrp1200.py':param_inv,
        }
        for program in program_accounting_plus:
            try:
                proses = [
                    ['python', "%s"%(os.path.join(macro_dir,program)), "--mf=%s"%mf, "--param=%s"%param_dicts[program]]
                ]
                for i,x in enumerate(proses):
                    subprocess.call(x)
                    print("Finished: "+str(i)+" "+ program)
                message.append("Finished: %s at %s" % (
                    program,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ))
            except Exception as e:
                print("Error:" + program)
                message.append("Error: %s at %s" % (
                    program,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ))
                message.append("Exception: %s" % e ) 
        pass


for m in message:
    print(m)
