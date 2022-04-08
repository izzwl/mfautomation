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


os.chdir('..')
os.chdir('macro')
files = []
tgl = param
NAMA_FILE = 'KEKJK'+'-'+tgl.replace(' ','_')
macro = ['ldb0103a','ldb0103g']

for m in macro:
    _param = param
    filename = m.upper()+'-'+param.replace(' ','_')
    _args = [
        '',
        '--param='+_param,
        '--output='+filename,
        '--mf='+mf_param,
        '--runxls=n',
    ]
    files.append(filename)
    sys.argv = _args
    # ldbexec = execfile('./'+m+'.py')
    ldbexec = None


file_kekjk = open(os.path.join(MFOUTLIST_DIR,NAMA_FILE), "w+")
file_kekjk.write('')
file_kekjk.close()
has_header = False
has_header_libur = False
header = ''
header_libur = ''
for f in files:
    file_kekjk = open(os.path.join(MFOUTLIST_DIR,NAMA_FILE), "a+")
    filetambahan = open(os.path.join(MFOUTLIST_DIR,f), "r")
    s = 0
    lines = filetambahan.readlines()
    org = ''
    for i,l in enumerate(lines):
       file_kekjk.write(l)
    file_kekjk.close()


os.chdir('..')
os.chdir('export')
sys.argv = [
    '',
    '--input_ldb0103a='+files[0],
    '--input_ldb0103g='+files[1],
    '--output='+NAMA_FILE+'.xls',
]
execfile(__file__)