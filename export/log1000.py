import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'LOG1000'
filename = args.output if args.output else 'LOG1000.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'MATERIAL-KELAS','PART-NUMBER','CD','SER','SANDI','DESCRIPTION','OWN','C','S','BIN#','STOCK-AWAL','STOCK-AKHIR','UOM','TGL-AWAL','KD-ASAL','EX-WIP','EX-CUST','PPCL#','CATATAN','SERIAL#'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,22,43,46,50,56,87,91,93,95,106,116,128,132,141,149,158,166,189,210,230,
])
export.set_date_col0([13,])
export.set_num_col0([10,11,])
export.export()
