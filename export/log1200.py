import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'LOG1200'
filename = args.output if args.output else 'LOG1200.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'TANGGAL','PART-NUMBER','LOKASI','QTY','UOM','EX-WIP','CUST',
    'CUST-NAME','EX-PPCL#','UNIT-PRICE','CUR','COND','REMARK',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,10,31,42,51,56,65,69,95,119,134,138,145,165,
])
export.set_date_col0([0])
export.set_num_col0([3,9])
export.export()
