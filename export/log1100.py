import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'LOG1100'
filename = args.output if args.output else 'LOG1100.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'PTR#','DATE','TO-WIP#','TO-ORG','DESCRIPTION','PART-DESCRIPTION',
    'PART-NUMBER','ISSUED-QTY','LOKNO','SERIAL#','TSN','TSO','CSN',
    'CSO','OWN','REMARK','EX-WIP','UNIT-PRICE','CUR','WOM','CUST',
    'NIK-APPR'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,11,19,27,35,61,97,118,129,140,156,165,174,180,186,190,
    211,219,234,238,245,250,258
])
export.set_date_col0([1,])
export.set_num_col0([7,17])
export.export()
