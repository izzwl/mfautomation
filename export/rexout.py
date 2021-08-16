import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'REXOUT'
filename = args.output if args.output else 'REXOUT.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'PART-NUMBER','DESCRIPTION','C','REQ#','ISSUED','QTY','MR#','GRN#','BIN#','WOM#','SERIAL#',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,22,58,60,71,79,89,98,109,120,127,145,
])
export.set_date_col0([4])
export.set_num_col0([5])
export.export()
