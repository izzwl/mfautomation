import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'MAB0340A'
filename = args.output if args.output else 'MAB0340A-MHT.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'TMWO#','WOM#','S','TOP','JML-MH','MAT-IN-RPH','M/H-IN-RPH','TOT-IN-RPH','MAT-AVG-USD','M/H-IN-USD','TOT-IN-USD','','MAT-IN-USD','MESIN-IN-USD'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,11,17,24,27,37,56,75,94,113,126,141,142,157,174
])
export.set_date_col0([])
export.set_num_col0([4,5,6,7,8,9,10,12,13])
export.set_text_col0([])
export.export()
