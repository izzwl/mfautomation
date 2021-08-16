import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR7007C'
filename = args.output if args.output else 'IVR7007C.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NP#','NIK','PRINTED','S','PG','REF','C','BENTUK','MTU','TOTAL-AMOUNT','S-PJK','NOTA-PJK#','SALDO-PJK','VENDOR','NAMA-VENDOR','VOUCHER#','DATE','BAYAR#','DATE','NILAI-BAYAR','SBU','BAYAR#','DATE','NILAI-BAYAR','BAYAR#','DATE','NILAI-BAYAR','BAYAR#','DATE','NILAI-BAYAR','BAYAR#','DATE','NILAI-BAYAR','BAYAR#','DATE','NILAI-BAYAR','NIK-APPR','TGL-APPR'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,11,18,26,29,33,44,46,53,56,73,80,91,107,115,141,151,159,169,176,194,198,209,216,234,245,252,270,281,288,306,317,324,342,353,360,378,388,296
])
export.set_date_col0([2,16,18,22,25,28,31,34,37])
export.set_num_col0([9,12,19,23,26,29,32,35,])
export.export()
