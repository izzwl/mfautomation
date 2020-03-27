import datetime
import subprocess
import os,sys

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
    'ivr7050m.py'   : [5],
}
mf = ''
try :
    mf = sys.argv[1]
except:
    pass

macro_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'macro',)
# print(macro_dir)
message = []
now = datetime.datetime.now()
ew  = now.strftime("%w") 
for program,hari in program_hari.items():
    try:
        if int(ew) in hari:
            subprocess.call(['python', "%s"%(os.path.join(macro_dir,program)), mf ])
            print("Finished:" + program)
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

for m in message:
    print(m)
