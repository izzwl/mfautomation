import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR7006A'
filename = args.output if args.output else 'IVR7006A.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'BP#','CREATED','MASTER#','VENDOR','DESCRIPTION','MTU','TOTAL-AMOUNT','NP#','DATE','VOUCHER#','DATE','BAYAR#','DATE'
])
export.set_firstlinedata(1)
export.set_popotongan([
    1,11,19,29,36,57,60,78,89,97,107,115,125,132
])
export.set_date_col0([1,8,10,12])
export.set_num_col0([6])
export.export()
