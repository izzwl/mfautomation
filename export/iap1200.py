import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IAP1200'
filename = args.output if args.output else 'IAP1200.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NOTA#','JNS','STS','CREATED','NIK-NOTA','MTU','NILAI-NOTA',
    'VEND/NIK','NAMA','SNDI','PG','WOM#','ORG','SBU','NILAI-NOTA-RPH',
    'VOUCHER#','DATE','BAYAR#','DATE','URAIAN','NO-REFERENSI','KH',
    'SALDO-PJK','SALDO-PJK-BM',
])
export.set_firstlinedata(3)
export.set_popotongan([
    1,10,13,18,25,34,39,57,67,88,93,97,104,111,114,132,142,150,161,
    169,220,241,243,261,279
])
export.set_date_col0([3,16,18,])
export.set_num_col0([4,14,22,23])
export.export()
