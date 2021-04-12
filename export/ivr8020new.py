import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR8020-NEW'
filename = args.output if args.output else 'IVR8020-NEW.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'MATERIAL-CLASS','NOMOR','PART-NUMBER','C','S','DESCRIPTION','OWN','QPA','BIN#','STOCK','','DATE','REMARK/PO#','PO-PRICE-USD','PRICE-LIST','TH','HS#','BM','PPN',
])
export.set_popotongan([
    0,21,28,47,49,51,72,76,80,91,99,103,111,127,140,154,159,170,177,185,
])
export.set_date_col0([11])
export.set_num_col0([9,13,14])
export.export()
