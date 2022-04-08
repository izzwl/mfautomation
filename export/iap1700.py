import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IAP1700'
filename = args.output if args.output else 'IAP1700.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'BM#','DATE','PJK#','DATE','UM#','DATE','VOUCHER#','DATE','BAYAR#','DATE',
    'PO#','MTU','NILAI-UM','SALDO-PJK-UM','SALDO-PJK-BM','VOUCHER-BM',
    'VEND/NIK','NAMA','COST-CENTER','NILAI-PJK','NILAI-PJK-CASH',
])
export.set_firstlinedata(3)
export.set_popotongan([
    1,11,19,29,37,47,55,65,73,83,91,100,104,129,149,169,183,192,213,219,243,263
])
export.set_date_col0([1,3,5,7,9,])
export.set_num_col0([12,13,14,19,20])
export.export()
