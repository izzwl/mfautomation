import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'PPB1300D'
filename = args.output if args.output else 'PPB1300D.xls'

export = xlsExport(outlist,filename)
# export.set_header([])
export.set_firstlinedata(0)
export.set_popotongan([
    1,22,43,47,55,61,82,87,92,113,118,123,143
])
export.set_date_col0([])
export.set_num_col0([2])
export.export()
