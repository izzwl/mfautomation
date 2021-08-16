import argparse
import os
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IAP1100'
filename = args.output if args.output else 'IAP1100.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','VOUCHER#','VOID','JNS','CREATED','NOTA#','DATE','SANDI','NILAI-NOTA',
    'URAIAN','REF-NOTA','NO-BAYAR','TANGGAL','INVOICE#','DATE','SNDI','PG',
    'WOM#','ORG','SBU','NIK/VENDOR','PJK','KDORG','MTU','NILAI-VOUCHER',
    'T-KURS','NILAI-VOUCHER-RPH','NILAI-PPH','S','NILAI-PPN','S','SALDO-PJK',
    'TERIMA','UMUR','VENDOR-BANK','PRINTED','VOIDED','KH','DUE-DATE-NP',
    'DUE-DATE-VCR','NO-PPN','NO-PPH'
])
export.set_firstlinedata(3)
export.set_popotongan([
    1,6,16,21,25,33,43,51,56,76,127,137,148,156,177,185,190,193,200,207,212,
    234,238,244,247,267,274,293,310,313,330,333,351,361,367,483,491,499,502,
    514,530,541,552,
])
export.set_date_col0([4,6,12,14,25,32,35,36,38,39])
export.set_num_col0([8,24,26,27,29,31])
export.export()

