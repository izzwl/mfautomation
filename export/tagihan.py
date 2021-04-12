import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'TAGIHAN'
filename = args.output if args.output else 'TAGIHAN.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','NAMA-VENDOR','PO-NUMBER','INV-NUMBER','NO-VOUCHER','VAL',
    'NILAI-VOUCHER','SISA-BAYAR','DATA-BANK','ACCOUNT#','ABA-IBA-NUM',
    'SBU','UMUR','PG','SANDI','REFERENSI','URGENT','RECEIVED',
    'DUE-DATE','TGL-VCHR'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,6,37,47,68,79,82,101,120,197,223,246,252,256,259,265,275,288,
    297,306,313
])
export.set_date_col0([17,18,19])
export.set_num_col0([6,7])
export.set_text_col0([3,9,10])
export.export()
