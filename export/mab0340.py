import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'MAB0340'
filename = args.output if args.output else 'MAB0340.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'WIP#','ST','TPROC','TYPE-DESCRIPTION','MAT-IN-RPH','M/H-IN-RPH',
    'TOT-IN-RPH','MAT-IN-USD','M/H-IN-USD','TOT-IN-USD','','WOM#','PART#',
    'QTY'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,9,12,18,37,56,71,90,105,118,133,134,140,162,166
])
export.set_date_col0([])
export.set_num_col0([4,5,6,7,8,9])
export.set_text_col0([10,11])
export.export()
