import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'MAB0300B'
filename = args.output if args.output else 'MAB0300B.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'SHOP','WC','TMWO#','F','PART#','DESCRIPTION','TYPE#','TOP','CREATED','DUE-DATE','WOM#','S','TASK','START-DATE','END-DATE','DAYS','LT','OWN','PG'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,6,9,17,19,40,61,72,76,85,94,101,103,108,119,127,134,140,144,148,
])
export.set_date_col0([8,9,13,14])
export.set_num_col0([15,16])
export.set_text_col0([2,4,10,11])
export.export()
