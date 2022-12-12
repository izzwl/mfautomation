import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'AVR8020K'
filename = args.output if args.output else 'AVR8020K.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','MATERIAL-KELAS','PART-NUMBER','P','DESCRIPTION','USE-CODE(APPLY)',
    'OWN','C','BIN#','STOCK','','UNIT-PRICE-AVG','EXT-PRICE-AVG','STORED',
    'RV#','PO#','ITM','PR#','WOM#','STS','CLOSED','CUST','SERIAL#','S',
    'I','SALE','UNIT-PRICE-USD','QPA','PRICE-LIST','TH','P','T','UPDATE',
    'SANDI','REQ#','REQ-BY','PRICE-ORD-RPH','EXT-ORD-RPH','UNIT-PRICE-AVG-USD',
    'EXT-PRICE-AVG-USD','VENDOR','NAMA-VENDOR','PO-S-3','DAP','DOKUMEN',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,6,27,49,51,87,108,112,114,125,133,136,152,167,176,185,193,198,
    207,214,218,226,231,252,254,256,261,276,279,292,296,298,300,308,
    314,324,339,354,370,382,403,415,446,454,458,482
])
export.set_date_col0([13,20,32,42])
export.set_num_col0([9,11,12,26,28,36,37,38,39,])
export.export()
