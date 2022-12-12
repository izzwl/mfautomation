import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR7007I'
filename = args.output if args.output else 'IVR7007I.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','NP#','CREATED','S','BP#','DATE','INVOICE#','MASTER#','PG','VENDOR','NILAI-BP','MTU','TOTAL-AMOUNT','VOUCHER#','DATE','BAYAR#','DATE','NILAI-BAYAR','SBU','BAYAR#','DATE','NILAI-BAYAR','BAYAR#','DATE','NILAI-BAYAR','BAYAR#','DATE','NILAI-BAYAR','BAYAR#','DATE','NILAI-BAYAR','BAYAR#','DATE','NILAI-BAYAR','NIK-APPR','TGL-APPR'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,6,16,23,26,36,44,71,80,83,109,124,128,146,163,172,182,189,207,212,222,229,247,258,266,283,294,302,319,330,338,355,366,374,391,401,409
])
export.set_date_col0([2,5,14,16,20,23,26,29,32,35])
export.set_num_col0([10,12,18,21,24,27,30,33])
export.export()
