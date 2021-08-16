import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR1711U'
filename = args.output if args.output else 'IVR1711U.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'PART-NUMBER','C','DESCRIPTION','USE-CODE(APPLY)','OWN','REQ-NUMBER','ISSUE-QTY','','UNIT-PRICE-USD','EXT-PRICE-USD','D/F','B','MATERIAL-KELAS','RV#','STORED','ISSUED','EXT-PRICE-AVG','EXT-PRICE-AVG-USD',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,24,26,57,78,82,93,100,103,117,133,138,140,161,171,181,188,208,226,
])
export.set_date_col0([14,15])
export.set_num_col0([6,8,9,16,17])
export.export()
