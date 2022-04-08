import argparse
import os,sys,re
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR8020A'
filename = args.output if args.output else 'IVR8020A.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'MATERIAL-KELAS','PART-NUMBER','C','S','DESCRIPTION','OWN',
    'QPA','C','BIN#','STOCK','','2021','2020','2019','2018','REMARK',
    'PO#','PRICE-USD','EXT-PRICE-USD','TGL-ASAL','TGL-AKHIR',
    'EXP-DATE','SANDI','USE-CODE(APPLY)','F','QTY','SERIAL#',
    'TSN','TSO','CSN','CSO',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,22,43,45,47,83,87,91,93,103,112,115,121,127,133,139,155,
    163,174,189,199,208,217,224,240,242,246,262,271,280,286,291
])
export.set_date_col0([19,20,21])
export.set_num_col0([9,11,12,13,14,17,18])
export.export()
