import datetime
import subprocess,sys
from x3270if import *
HOST = 'mainframe' # 'hercules' or 'mainframe'
PORT = '5000'

# FILE='/home/hercules/mfoutlist/BCINBC23'
FILE='/home/hercules/mfoutlist/BCMR02'
JCL="IMSVS.PROD.BMP(BCMR02)"
TSO_USER = "TSO MPMCS99"
end = datetime.datetime.now()
if end.strftime("%-d") == '1' or (end.strftime("%-d") in ['2','3'] and end.strftime("%w") == '1' ):
    begin = datetime.datetime.now() + datetime.timedelta(days=-31)
elif end.strftime("%w") == '1':
    begin = datetime.datetime.now() + datetime.timedelta(days=-16)
else:
    begin = datetime.datetime.now() + datetime.timedelta(days=-14)
PARAM_INTERVAL = "%s %s" % (begin.strftime("%y%m%d"),end.strftime("%y%m%d"))

def handle():
    cek_konek(PORT)
    string(PORT,TSO_USER)
    enter(PORT)
    enter(PORT)
    enter(PORT)
    enter(PORT)
    cek_logon(PORT)
    string(PORT,"P.2")
    enter(PORT)
    tab(PORT)
    string(PORT,JCL)
    enter(PORT)
    string(PORT,"RES")
    enter(PORT)
    movecursor(PORT,5,10)
    string(PORT,"MPMCS99I")
    movecursor(PORT,6,60)

    if HOST == 'hercules':
        string(PORT,"MPMCS99           ")
    elif HOST == 'mainframe':
        string(PORT,"MPMCS99")

    movecursor(PORT,19,8)
    string(PORT,PARAM_INTERVAL)
    movecursor(PORT,3,14)
    string(PORT,"SUB")
    enter(PORT)

    job = job_info(PORT)

    print(job)

    while True:
        enter(PORT)
        result = job_result(PORT,job)
        print(result)

        if result[0]:
            break
        subprocess.Popen("sleep 2",shell=True).wait()

    rc_code = result[0].find("MAXCC=0")
    if rc_code > 1:
        print(result[0])
    else:
        sys.exit(result[0])

    enter(PORT)
    enter(PORT)
    pf(PORT,3)
    pf(PORT,3)
    pf(PORT,3)
    string(PORT,"SD.H")
    enter(PORT)

    rows = sd_h_row(PORT,job)
    row = int(rows[0])-1
    movecursor(PORT,row,1)
    string(PORT,"XDC")
    enter(PORT)
    enter(PORT)
    movecursor(PORT,23,20)

    string(PORT,"/\$P JQ,JM=MPMCS99*")
    enter(PORT)
    enter(PORT)
    enter(PORT)

    pf(PORT,3)
    pf(PORT,3)
    string(PORT,"P.2")
    enter(PORT)
    tab(PORT)
    string(PORT,"mpmcs99.transfer")
    enter(PORT)
    string(PORT,"RES")
    enter(PORT)
    string(PORT,"c x'00' ' ' all")
    enter(PORT)
    pf(PORT,3)
    pf(PORT,3)
    string(PORT,"6")
    enter(PORT)
    transfer(PORT,FILE)
    pf(PORT,3)
    pf(PORT,3)
    pf(PORT,3)
    string(PORT,"2")
    enter(PORT)
    string(PORT,"logoff")
    enter(PORT)

    return 'ALHAMDULILLAH'
