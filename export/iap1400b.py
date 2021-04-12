import argparse
import os
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IAP1400B'
filename = args.output if args.output else 'IAP1400B.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'JENIS','NO-PENR.','CREATED','NIK','SBU','SANDI','PG','INVOICE#','CUSTOMER','NOMOR-REF.','TANGGAL','NO-REK-UMC','NAMA-BANK','MTU','TOTAL-BAYAR','REMARK'
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,9,18,26,33,38,44,47,57,61,88,104,112,133,154,157,179,225
])
export.set_date_col0([2,11,])
export.set_num_col0([15])
export.export()
