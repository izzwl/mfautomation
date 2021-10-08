import argparse
import os,sys,re
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR1321B'
filename = args.output if args.output else 'IVR1321B.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'REQ-NUMBER','ISSUED','REQ-BY','PART-NUMBER','C','DESCRIPTION','EX-CD','QTY','','MATERIAL-CLASS','EXT-PRICE-USD','EXT-PRICE-RPH','KD-ORG',
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,12,20,27,45,47,63,68,76,79,94,111,130,141
])
export.set_date_col0([1])
export.set_num_col0([7,10,11])

export.get_raw_lines()
raw_lines = export.raw_lines
new_raw_lines = []
for i,l in enumerate(raw_lines):
    m = re.match(r'[0-9]{6}',l[5:11])
    if ( m and m.span()[1]==len(l[5:11]) ):
        new_raw_lines.append(l)
export.override_raw_lines = new_raw_lines

export.export()
