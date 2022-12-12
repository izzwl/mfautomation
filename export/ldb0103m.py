import argparse
import os,sys,re
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'LDB0103M'
filename = args.output if args.output else 'LDB0103M.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO','NIK','NAMA','DWC/CATAT',' ','AVAILABLE-HOURS','JAM-KERJA-DU',
    'CAJ-HOURS-REGULER','CAJ-HOURS-OVERTIME','TOTAL','900025-REGULER',
    '900025-OVERTIME','TOTAL','WIP-HOURS-REGULER','WIP-HOURS-OVERTIME',
    'TOTAL','%DARI-AVAILABLE','%DARI-JK(DU)','KD-ORG','NAMA-ORG','D/I'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,6,13,28,32,36,46,56,66,75,85,95,104,114,124,133,143,150,160,169,
    190,193
])
export.set_date_col0([])
export.set_num_col0([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
export.get_raw_lines()
raw_lines = export.raw_lines
new_raw_lines = []
for i,l in enumerate(raw_lines):
    m = re.match(r'[0-9]{6}',l[6:12])
    if ( m and m.span()[1]==len(l[6:12]) ):
        new_raw_lines.append(l)
export.override_raw_lines = new_raw_lines
export.export()
