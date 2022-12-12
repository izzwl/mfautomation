import argparse
import os,sys,re
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR8020C'
filename = args.output if args.output else 'IVR8020C.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','PART-NUMBER','DESCRIPTION','BIN','STOCK','','','EXP-DATE','DAYS','SCRAP','EXT-DATE','APPROVED-BY',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,8,31,59,70,81,84,87,95,101,112,122,133
])
export.set_date_col0([7,10])
export.int_col0 = [0,8]
export.set_num_col0([4])
# export.end_line_regex ="^.*RESUME - ORG$"
# export.end_line_regex_offset = -3

export.get_raw_lines()
raw_lines = export.raw_lines
new_raw_lines = []
for i,l in enumerate(raw_lines):
    try:
        int(l[1:7].strip())
        new_raw_lines.append(l)
    except:
        pass
export.override_raw_lines = new_raw_lines
export.export()
