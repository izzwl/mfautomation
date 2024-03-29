import argparse
import os,sys,re
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'TLB1030'
filename = args.output if args.output else 'TLB1030.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','TOOL #','METNO','DESCRIPTION','CAPACITY','UOM','MFG NAME',
    'DUEDATE','ST','DAY','AREA','WC','C','START','COMPLETE'
])
export.set_firstlinedata(1)
export.set_popotongan([
    3,8,16,25,42,58,65,77,86,90,95,101,104,106,114,126
])
export.set_date_col0([7,13,14])
export.set_num_col0([])

export.get_raw_lines()
raw_lines = export.raw_lines
new_raw_lines = []
for i,l in enumerate(raw_lines):
    m = re.match(r'[0-9]{6}',l[9:15])
    if ( m and m.span()[1]==len(l[9:15]) ):
        new_raw_lines.append(l)
export.override_raw_lines = new_raw_lines

export.export()
