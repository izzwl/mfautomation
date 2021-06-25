import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'VRP1100A'
filename = args.output if args.output else 'VRP1100A.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'WIP#','CREATE','S','PG','JOB','CUST','OPENED','CLOSED','VOUCHER#','CREATED','SANDI','NIK/VEND','NAMA','MTU','NILAI','NILAI(RPH)','NILAI(USD)','PAYMENT#','REF-VCHR','URAIAN'
])
export.set_firstlinedata(4)
export.set_popotongan([
    1,8,15,17,20,24,29,37,45,55,63,69,78,104,108,125,144,163,175,185,300,
])
export.set_date_col0([6,7,9])
export.set_num_col0([14,15,16])
export.export()
