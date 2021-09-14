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

MFOUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')

DEPT = [
    'A1100 A1110 A1120 A6410 A6710      ',
    'U3110 U3120 U3130 U3140 U3150 U3160',
    'U3410 U3420 U3430 U3440 U3800 U3810',
]

os.chdir('..')
os.chdir('macro')
files = []
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

# os.chdir('..')
# os.chdir('export')
# sys.argv = ['','--input='+NAMA_FILE,'--output='+NAMA_FILE+'.xls']
# print(sys.argv)
# dir()
# ldbexec = execfile('ldb0105b.py')