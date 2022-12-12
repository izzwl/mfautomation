import argparse
import os,sys,re
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'VRP1900-DETAIL'
filename = args.output if args.output else 'VRP1900-DETAIL.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'WIP#','X','CREATD','PG','CUS','W','T','P','C','JOB','OPENED',
    'CLOSED','Q-REST','TMWO','SALDO-WIP-MH','SALDO-WIP-MAT',
    'SALDO-WIP','SERIAL#','DESCRIPTION','PENYESUAIAN-USD-WOM',
    'SALDO-WIP-MH-USD','SALDO-WIP-MAT-USD','SALDO-WIP-USD',
    'MESIN-IN-USD',
])
export.set_firstlinedata(1)
export.set_popotongan([
    1,7,10,17,20,24,26,28,30,32,36,43,52,59,66,81,100,120,142,163,181,206,225,244,259,
])
export.set_date_col0([10,11])
export.set_num_col0([14,15,16,19,20,21,22])
export.export()
