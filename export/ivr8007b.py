import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR8007B'
filename = args.output if args.output else 'IVR8007B.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'PART-NUMBER','C','I','DESCRIPTION','QPA','MAX','ROP','LEAD','RECQ',
    'RESERVE','STOCK','ALT-STOCK',' ','2020','2019','2018','2017','Q-PR',
    'ALT-PR','BLNCPO','MATERIAL-KELAS','SPQ','ROT-STOCK','PO#','ITM',
    'MTU','UNIT-PRICE'
])
export.set_firstlinedata(3)
export.set_popotongan([
    1,20,22,24,39,43,48,53,57,63,69,77,86,90,95,101,107,113,119,125,
    132,155,162,173,182,186,190,204
])
export.set_date_col0([])
export.set_num_col0([4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,22,26])
export.export()
