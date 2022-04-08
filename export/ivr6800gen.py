import argparse
import os
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

MFOUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')
outlist = args.input if args.input else 'IVR6800PRE'
filename = args.output if args.output else 'IAP1100.xls'

DST = {
    'IVR6800-REALPR':3,
    'IVR6800-REALPO':4,
    'IVR6800-ANGGARAN':5,
}

f = open(os.path.join(MFOUTLIST_DIR,outlist), "r")
lines = f.readlines()

for k,v in DST.items():
    nf = open(os.path.join(MFOUTLIST_DIR,k), "w+") 
    for l in lines:
        ls = l.split(" ")
        nl = ls[0].strip()+ls[1].strip()+" "+ls[2].strip()+" "+ls[v].strip().replace(".","").rjust(17,"0")+"\n"
        nf.write(nl)
    nf.close()
        

