import datetime
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--param', help='210801 210831')
parser.add_argument('--mf', help='mf instance (ibm / hrc)')
# parser.add_argument('--user', help='MPMCS32')
# parser.add_argument('--output', help='output file name')
args = parser.parse_args()

if not args.param:
    exit('param not set')
param = args.param
mf_param = args.mf or 'ibm'

bulan = param[2:4]
tahun = param[0:2]

MFOUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')

DEPT = [
    'A1100 A1110 A1120 A6710 A6410 A6430',
    'U3110 U3120 U3130 U3140 U3150 U3160',
    'U3410 U3420 U3430 U3440 U3800 U3810',
]

os.chdir('..')
os.chdir('macro')
files = []
files = ['211001_211031-LDB0105B0','211001_211031-LDB0105B1','211001_211031-LDB0105B2']
tgl = param
for i,d in enumerate(DEPT):
    _param = "%s %s"%(tgl,d)

    # args.param.replace(' ','_') = 'MAY21'
    # param = "%s %s"%('210501 210531',d)

    filename = tgl.replace(' ','_')+'-'+'LDB0105B'+str(i)+''
    _args = [
        '',
        '--user=mpmcs99',
        '--param='+_param,
        '--output='+filename,
        '--mf='+mf_param,
    ]
    files.append(filename)
    sys.argv = _args
    # print(sys.argv)
    ldbexec = execfile('./ldb0105b.py')
    ldbexec = None

NAMA_FILE = tgl.replace(' ','_')+'-'+'LDB0105B'
_NAMA_FILE = tgl.replace(' ','_')+'-'+'LDB0105BR'
fileasli = open(os.path.join(MFOUTLIST_DIR,NAMA_FILE), "w+")
fileasli.write('')
fileasli.close()
has_header = False
has_header_libur = False
header = ''
header_libur = ''
for f in files:
    fileasli = open(os.path.join(MFOUTLIST_DIR,NAMA_FILE), "a+")
    filetambahan = open(os.path.join(MFOUTLIST_DIR,f), "r")
    s = 0
    lines = filetambahan.readlines()
    org = ''
    for i,l in enumerate(lines):
        if 'ORGANISASI   :' in l:
            org = l[63:68]

        if not has_header:
            try:
                if 'NO. N I K  N A M A' in l:
                    # fileasli.write(l)
                    has_header = True
                    header = l
            except:
                pass
        
        if not has_header_libur:
            try:
                if '~~' in l:
                    # fileasli.write(l)
                    has_header_libur = True
                    header_libur = l
            except:
                pass

        try:
            if int(l[1:4].strip()) and l[4:5]==' ':
                l = org.ljust(5,' ')+l[5:].replace('\n','')+'\n'
                fileasli.write(l)
        except:
            pass
    # fileasli.write(filetambahan.read())

fileasli.close()

_fileasli = open(os.path.join(MFOUTLIST_DIR,_NAMA_FILE), "w+")
_fileasli.write('')
fileasli = open(os.path.join(MFOUTLIST_DIR,NAMA_FILE), "r")
lines = fileasli.readlines()

for i,l in enumerate(lines):
    identity = l[0:40]
    hari = header[40:]
    sts_hari = l[40:]
    list_hari = []
    for i in range(0,len(hari),3):
        tgl = header[40:][i:i+3].strip()
        libur = header_libur[40:][i:i+3].strip()
        try:
            sts = sts_hari[i:i+3].strip()
        except:
            sts = ''
        sts = sts.ljust(2,' ')
        tx = tahun+bulan+tgl+' '+sts+libur.ljust(2,' ')
        list_hari.append(tx)
    for lh in list_hari:
        tx = identity.strip().ljust(40,' ')+lh+'\n'
        _fileasli.write(tx)

_fileasli.close()
# os.chdir('..')
# os.chdir('export')
# sys.argv = ['','--input='+NAMA_FILE,'--output='+NAMA_FILE+'.xls']
# print(sys.argv)
# dir()
# ldbexec = execfile('ldb0105b.py')