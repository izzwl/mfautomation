import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'LDB0501B'
filename = args.output if args.output else 'LDB0501B.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'WOM','WIP','TYPROC','PART','DESCRIPTION','CREATED','CLOSED','REGULAR','OVER-TIME','TOTAL','STANDARD'
])
export.set_firstlinedata(1)
export.set_popotongan([
    1,8,17,25,48,61,71,82,94,108,119
])
export.set_date_col0([])
export.set_num_col0([6,7,8,9,])
export.export()
