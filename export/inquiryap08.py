import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'AP08DATA'
filename = args.output if args.output else 'AP08DATA.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'WIP','MAT-IDR','MAT-USD','M/H','M/H-IDR','M/H-USD','OTH-IDR','OTH-USD',
])
export.set_firstlinedata(0)
export.set_popotongan([
    # 0,7,27,49,71,93,115,137
    0,7,28,49,70,91,112,133,153,
])
export.set_date_col0([])
export.set_int_col0([0])
export.set_num_col0([1,2,3,4,5,6,7])
export.export()
