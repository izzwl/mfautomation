import argparse
import os,sys,re
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'MAB0340'
filename = args.output if args.output else 'MAB0340.xls'

export = xlsExport(outlist,filename)

#Sheet MAB
export.first_line_regex = "^  WIP#    ST TPROC TYPE-DESCRIPTION"
export.first_line_regex_offset = 1
export.end_line_regex = "^                               TOTAL:"
export.set_header([
    'WIP#','ST','TPROC','TYPE-DESCRIPTION','MAT-IN-RPH','M/H-IN-RPH',
    'TOT-IN-RPH','MAT-IN-USD','M/H-IN-USD','TOT-IN-USD','','WOM#','PART#',
    'QTY'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,9,12,18,37,56,71,90,105,118,133,134,140,162,166
])
export.set_date_col0([])
export.set_num_col0([4,5,6,7,8,9])
export.set_text_col0([10,11])

export.get_raw_lines()
raw_lines = export.raw_lines
new_raw_lines = []
for i,l in enumerate(raw_lines):
    m = re.match(r'[0-9]{7}',l[1:8])
    if ( m and m.span()[1]==len(l[1:8]) ):
        new_raw_lines.append(l)
export.override_raw_lines = new_raw_lines

export.export_ws('MAB0340')
export.save_export()


#Sheet PROFIT
export.ws = export.wb.add_sheet('PROFIT')
export.first_line_regex = "^1OWNER"
export.first_line_regex_offset = -1
export.end_line_regex = None
export.set_header([
    '','QUOTATION','AP08(USD)','AP08(RPH)','DELTA','PROFIT'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,31,46,62,82,98,128
])
export.set_date_col0([])
export.set_num_col0([1,2,3,4,5])
export.num_col0_remove_zero = [1,2,3,4,5]
export.set_text_col0([])
export.override_raw_lines = []
export.get_raw_lines()
raw_lines = export.raw_lines

row = 1
for i in range(5):
    export.ws.write(row,0,raw_lines[i][1:31].strip())
    export.ws.write(row,1,raw_lines[i][31:80].strip())
    row += 1
row += 1
export.raw_lines = raw_lines[5:]
export.write_body(row=row)
export.auto_width()
export.save_export()
