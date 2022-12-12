import argparse
import datetime
import os
import xlwt

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

MFOUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')
MFXLS_DIR = os.path.join(os.path.expanduser("~"),'mfxls')
outlist = os.path.join(MFOUTLIST_DIR,'%s'%(args.input if args.input else 'LDB0103A' ))
filename = "%s.xls"%(args.output if args.output else 'LDB0103A' )

wb = xlwt.Workbook(encoding='utf-8',style_compression=2)
ws = wb.add_sheet('Sheet 1')
# Sheet header, first row
row_num = 0

font_style = xlwt.XFStyle()
font_header_style = xlwt.easyxf('font: bold true; borders: left thin, right thin, top thin, bottom thin;')
font_body_style = xlwt.easyxf('borders: left thin, right thin, bottom thin;')
# font_style.font.bold = True

header = [
    'NIK','NAMA','GR','ORG','NAMA-ORG','TGL','KD','J-DAT','J-PUL','LDAT','LPUL',
    'LTOT','LIBUR','LBH-T','LBH-L','ATH'
]
for col_num in range(len(header)):
    ws.write(row_num, col_num, header[col_num], font_style)


no = 0
row = 1

f = open(outlist, "r")
s = 0
lines = f.readlines()
for i,l in enumerate(lines):
    if l[1:7].strip().isdigit():
        col = 0
        ws.write(row, col+0, l[1:7].strip(), font_style)
        ws.write(row, col+1, l[8:39].strip(), font_style)
        ws.write(row, col+2, l[39:42].strip(), font_style)
        ws.write(row, col+3, l[42:48].strip(), font_style)
        ws.write(row, col+4, l[48:74].strip(), font_style)
        ws.write(row, col+5, l[74:82].strip(), font_style)
        ws.write(row, col+6, l[82:85].strip(), font_style)
        ws.write(row, col+7, l[85:91].strip(), font_style)
        ws.write(row, col+8, l[91:97].strip(), font_style)
        ws.write(row, col+9, l[97:102].strip(), font_style)
        ws.write(row, col+10, l[102:107].strip(), font_style)
        ws.write(row, col+11, l[107:112].strip(), font_style)
        ws.write(row, col+12, l[112:118].strip(), font_style)
        ws.write(row, col+13, l[118:124].strip(), font_style)
        ws.write(row, col+14, l[124:130].strip(), font_style)
        ws.write(row, col+15, l[130:132].strip(), font_style)
        row += 1

wb.save(os.path.join(MFXLS_DIR, filename))