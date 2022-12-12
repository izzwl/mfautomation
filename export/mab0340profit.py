import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'MAB0340'
filename = args.output if args.output else 'MAB0340-Profit.xls'

export = xlsExport(outlist,filename)
export.set_header([
    '','QUOTATION','AP08(USD)','AP08(RPH)','DELTA','PROFIT'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,31,46,62,82,98,128
])
export.set_date_col0([])
export.set_num_col0([1,2,3,4,5])
export.set_text_col0([])
export.export()
