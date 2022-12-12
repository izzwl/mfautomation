import argparse
import os,sys,re
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR1325'
filename = args.output if args.output else 'IVR1325.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'REQ-NUMBER','DATE','REQ-BY','AUTH-BY','USER','PART-NUMBER','C','DESCRIPTION','REQ-QTY','','RESV-QTY','STOCK-QTY','','PR-QTY','BLNC-PO','MAT-CLASS','PR#','PO#','NEED-DTE','KD-ORG'
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,12,20,27,35,41,59,61,73,80,82,91,100,103,111,119,141,150,159,168,174,
])
export.set_date_col0([1,18])
export.set_num_col0([8,10,11,13,14])

export.get_raw_lines()
raw_lines = export.raw_lines
new_raw_lines = []
for i,l in enumerate(raw_lines):
    m = re.match(r'[0-9]{6}',l[20:26])
    if ( m and m.span()[1]==len(l[20:26]) ):
        new_raw_lines.append(l)
export.override_raw_lines = new_raw_lines

export.export()
