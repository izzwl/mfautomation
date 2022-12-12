import argparse
import os,sys,re
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'GATELBR'
filename = args.output if args.output else 'GATELBR.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NIK','NAMA','KD-ORG','TANGGAL','OUT','IN','MENIT','IST','SIK',
    'URAIAN-KEPERLUAN-DINAS',
])
export.set_firstlinedata(1)
export.set_popotongan([
    1,9,36,44,53,60,67,75,79,83,105
])
export.set_date_col0([3])
export.set_num_col0([])

export.end_line_regex ="^.*RESUME - ORG$"
export.end_line_regex_offset = -3

export.get_raw_lines()
raw_lines = export.raw_lines
new_raw_lines = []
for i,l in enumerate(raw_lines):
    m = re.match(r'[0-9]{6}',l[1:7])
    if ( m and m.span()[1]==len(l[1:7]) ):
        new_raw_lines.append(l)
export.override_raw_lines = new_raw_lines

export.export()
