import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'MAB0320B'
filename = args.output if args.output else 'MAB0320B.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'SHOP','WC','TMWO#','F','TASK','PART#','DESCRIPTION','TYPE#','TOP','CREATED','DUE-DATE','SINCE','FROM','WC','WOM#','S','TASK-STATUS','INT-BEGIN','INT-END','DAYS','REASON','NIK-WOM','CUST','REM-HRS'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,6,9,17,19,24,45,66,77,81,90,99,108,115,121,128,130,142,152,162,167,198,206,211,218,
])
export.set_date_col0([9,10,11,17,18])
export.set_num_col0([19,23])
export.set_text_col0([2,4,5,12,14])
export.export()
