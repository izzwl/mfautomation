import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'LDB0102D'
filename = args.output if args.output else 'LDB0102D.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','WIP','TYPNO','PART DESCRIPTION','TPROC','REGULAR','OVER-TIME','TOTAL','KDORG','WIP-WOM','PG','ATA',
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,8,15,26,58,64,76,86,99,107,118,125,128,
])
export.set_date_col0([])
export.set_num_col0([5,6,7])
export.export()
