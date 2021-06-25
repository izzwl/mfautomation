import datetime
import os
import sys
MFOUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')

DEPT = [
    'A1100 A1110 A1120 A6410 A6710      ',
    'U3110 U3120 U3130 U3140 U3150 U3160',
    'U3410 U3420 U3430 U3440 U3800 U3810',
]

tgl_awal = datetime.datetime(2021,5,30)
tgl_akhir = datetime.datetime(2021,5,31)

while tgl_awal <= tgl_akhir:
    os.chdir('..')
    os.chdir('macro')
    files = []
    for i,d in enumerate(DEPT):
        tgl = tgl_awal.strftime('%y%m%d')
        param = "%s %s %s"%(tgl,tgl,d)

        # tgl = 'MAY21'
        # param = "%s %s"%('210501 210531',d)

        filename = tgl+'-'+'LDB0103M'+str(i)+''
        args = [
            '',
            '--user=mpmcs99',
            '--param='+param,
            '--output='+filename,
            '--mf=hrc',
        ]
        files.append(filename)
        sys.argv = args
        # print(sys.argv)
        ldbexec = execfile('./ldb0103m.py')
        ldbexec = None
    
    NAMA_FILE = tgl+'-'+'LDB0103M'
    fileasli = open(os.path.join(MFOUTLIST_DIR,NAMA_FILE), "w+")
    fileasli.write('')
    fileasli.close()
    for f in files:
        fileasli = open(os.path.join(MFOUTLIST_DIR,NAMA_FILE), "a+")
        filetambahan = open(os.path.join(MFOUTLIST_DIR,f), "r")
        s = 0
        lines = filetambahan.readlines()
        for i,l in enumerate(lines):
            try:
                if int(l[1:4].strip()) and l[4:5]==' ':
                    fileasli.write(l)
            except:
                pass
        # fileasli.write(filetambahan.read())

    fileasli.close()
    os.chdir('..')
    os.chdir('export')
    sys.argv = ['','--input='+NAMA_FILE,'--output='+NAMA_FILE+'.xls']
    # sys.argv = [sys.argv[0]]
    print(sys.argv)
    dir()
    # ldbexec = execfile('ldb0103m.py')
    # ldbexec = None
    # del ldbexec
    # break
    tgl_awal += datetime.timedelta(days=1)