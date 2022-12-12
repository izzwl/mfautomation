import argparse
import os,sys,re
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'LDB0502B'
filename = args.output if args.output else 'LDB0502B.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'SEQ','WIP','TYP','PART-DESCRIPTION','CREATED','CLOSED','NIK',
    'NAME','ORG','DATE','REG','OVT','TOTAL'
])
export.set_firstlinedata(1)
export.set_popotongan([
    1,5,12,16,37,45,53,60,80,86,93,101,110,120
])
export.set_date_col0([4,5,9])
export.set_num_col0([10,11,12])
export.get_raw_lines()
raw_lines = export.raw_lines
new_raw_lines = []
for i,l in enumerate(raw_lines):
    m = re.match(r'[0-9]{6}',l[5:11])
    if ( m and m.span()[1]==len(l[5:11]) ):
        new_raw_lines.append(l)
export.override_raw_lines = new_raw_lines
export.export()
