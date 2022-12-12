import argparse
import os
import sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IAP1400D'
filename = args.output if args.output else 'IAP1400D.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'JENIS','NO-PENR.','CREATED','NIK','SBU','SANDI','PG','INVOICE#','CUSTOMER-CODE','CUSTOMER','NOMOR-REFERENSI','TGL-REF','MTU','TOTAL-BAYAR','KOMENTAR',
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,9,18,26,33,38,44,47,57,61,88,109,117,120,144,
])
export.set_date_col0([2,11,])
export.set_num_col0([13])
export.export()
