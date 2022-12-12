import argparse
import os,sys,re
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR1320B'
filename = args.output if args.output else 'IVR1320B.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NOMOR','REQ-NUMBER','ISSUE-DTE','WIP','PART-NUMBER','C','DESCRIPTION','ISSUE-QTY','','RETURN','MAT-CLASS','EXT-PRICE-USD',
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,8,19,30,38,59,61,80,87,90,99,114,132,
])
export.set_date_col0([2])
export.set_num_col0([7,9,11])

export.get_raw_lines()
raw_lines = export.raw_lines
new_raw_lines = []
for i,l in enumerate(raw_lines):
    m = re.match(r'[0-9]{6}',l[12:18])
    if ( m and m.span()[1]==len(l[12:18]) ):
        new_raw_lines.append(l)
export.override_raw_lines = new_raw_lines

export.export()
