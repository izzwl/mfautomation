import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'VRP1200'
filename = args.output if args.output else 'VRP1200.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'INVOICE#','CREATED','S','K','MS#','CREATED','WIP#','S','PG','JOB',
    'TYPE-NUMB','PART-NUMBER','SERIAL#','PO-NUMBER','BILL',
    'TOTAL-PRICE','CREDIT-SALE','MTU','DUE-DATE','PO-DATE',
    'TOT-QUOTATION','MTU','CREATED'
])
export.set_firstlinedata(4)
export.set_popotongan([
    1,11,19,21,23,32,40,47,49,52,56,66,80,92,113,117,137,158,163,172,179,
    197,201,208
])
export.set_date_col0([1,5,18,19,])
export.set_num_col0([15,16,20])
export.export()
