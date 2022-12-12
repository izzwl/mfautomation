import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'MCR3020A'
filename = args.output if args.output else 'MCR3020A.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'ORG','NIK','NAMA','DUE-DATE','','TMT-MASUK','TMT-KGG','TMT-CB',
    'CB','CT','CP','KB'
])
export.set_firstlinedata(0)
export.set_popotongan([
    2,9,17,39,48,51,63,75,87,91,97,101,103,
])
export.set_date_col0([3,5,6,7])
export.set_num_col0([])
export.set_text_col0([])
export.export()
