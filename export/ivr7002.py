import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR7002'
filename = args.output if args.output else 'IVR7002.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','CODE','DESCRIPTION','ADDRESS','ZIPCODE','TELP-NUMBER',
    'FAX-NUMBER','REP-NAME','D/F','CATEGORY','IPTN-REGR.','QUALITY',
    'MTU','VENDOR-BANK','ACCOUNT#','BANK-ABA#','VALID-DTE','PROGRAM',
    'QL','MOTHER'
])
export.set_firstlinedata(1)
export.set_popotongan([
    1,6,12,43,152,163,179,195,226,230,245,256,267,271,362,388,404,414,434,437
])
export.set_date_col0([16])
export.set_num_col0([])
export.export()
