import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'VOUCHER'
filename = args.output if args.output else 'VOUCHER.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','CREATED','NOTA#','SBU','VOUCHER#','NIK/VENDOR','NILAI-VOUCHER',
    'MTU','NO-BAYAR','PJK#','NILAI-PJK','SISA-PJK','BM#'
])
export.set_firstlinedata(1)
export.set_popotongan([
    1,6,14,24,29,39,66,85,90,99,109,127,147,156
])
export.set_date_col0([1,])
export.set_num_col0([6,9])
export.export()
