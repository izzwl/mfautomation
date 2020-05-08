import argparse
import datetime
import os
import xlwt
import re

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

MFOUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')
MFXLS_DIR = os.path.join(os.path.expanduser("~"),'mfxls')
outlist = os.path.join(MFOUTLIST_DIR,'%s'%(args.input if args.input else 'LDB0104C' ))
filename = "%s.xls"%(args.output if args.output else 'LDB0104C' )

wb = xlwt.Workbook(encoding='utf-8',style_compression=2)
ws = wb.add_sheet('Sheet 1')
# Sheet header, first row
row_num = 0

font_style = xlwt.XFStyle()
font_header_style = xlwt.easyxf('font: bold true; borders: left thin, right thin, top thin, bottom thin;')
font_body_style = xlwt.easyxf('borders: left thin, right thin, bottom thin;')
# font_style.font.bold = True

ws.write_merge(0,1,0,0,'ORG CODE', font_style)
ws.write_merge(0,1,1,1,'DESCRIPTION', font_style)
ws.write_merge(0,0,2,3,'LABOR', font_style)
ws.write(1,2,'I', font_style)
ws.write(1,3,'D', font_style)
ws.write_merge(0,0,4,7,'DAILY-WORK-CARD', font_style)
ws.write(1,4,'HARI-KERJA', font_style)
ws.write(1,5,'LEMBUR', font_style)
ws.write(1,6,'HARUS', font_style)
ws.write(1,7,'SALAH', font_style)
ws.write(0,8,'JAM', font_style)
ws.write(0,9,'JAM', font_style)
ws.write(1,8,'KEHADIRAN', font_style)
ws.write(1,9,'JAM LEMBUR', font_style)
ws.write_merge(0,0,10,12,'CAJ-HOURS', font_style)
ws.write(1,10,'REGULAR', font_style)
ws.write(1,11,'OVER-TIME', font_style)
ws.write(1,12,'TOTAL', font_style)
ws.write_merge(0,0,13,15,'900025-PERINTAH-LANGSUNG', font_style)
ws.write(1,13,'REGULAR', font_style)
ws.write(1,14,'OVER-TIME', font_style)
ws.write(1,15,'TOTAL', font_style)
ws.write_merge(0,0,16,18,'900009+900013(RAPAT+TRAINING)', font_style)
ws.write(1,16,'REGULAR', font_style)
ws.write(1,17,'OVER-TIME', font_style)
ws.write(1,18,'TOTAL', font_style)
ws.write_merge(0,0,19,21,'WIP-HOURS+900025+900009+900013', font_style)
ws.write(1,19,'REGULAR', font_style)
ws.write(1,20,'OVER-TIME', font_style)
ws.write(1,21,'TOTAL', font_style)
ws.write_merge(0,0,22,24,'WIP-HOURS', font_style)
ws.write(1,22,'REGULAR', font_style)
ws.write(1,23,'OVER-TIME', font_style)
ws.write(1,24,'TOTAL', font_style)

no = 0
row = 2

f = open(outlist, "r")
s = 0
lines = f.readlines()
for i,l in enumerate(lines):
    m = re.match(r'[A-Z]{1}[0-9]{4}',l[4:9])
    if ( m and m.span()[1]==len(l[4:9]) ) or  l[17:22] == 'TOTAL':
        col = 0
        ws.write(row, col+0, l[3:10].strip(), font_style)
        ws.write(row, col+1, l[10:25].strip(), font_style)
        ws.write(row, col+2, float(l[25:29].strip()), font_style)
        ws.write(row, col+3, float(l[29:34].strip()), font_style)
        ws.write(row, col+4, float(l[34:41].strip()), font_style)
        ws.write(row, col+5, float(l[41:47].strip()), font_style)
        ws.write(row, col+6, float(l[47:54].strip()), font_style)
        ws.write(row, col+7, float(l[54:59].strip()), font_style)
        ws.write(row, col+8, float(l[59:70].strip()), font_style)
        ws.write(row, col+9, float(l[70:81].strip()), font_style)
        ws.write(row, col+10, float(l[81:92].strip()), font_style)
        ws.write(row, col+11, float(l[92:101].strip()), font_style)
        ws.write(row, col+12, float(l[101:112].strip()), font_style)
        ws.write(row, col+13, float(l[112:123].strip()), font_style)
        ws.write(row, col+14, float(l[123:132].strip()), font_style)
        ws.write(row, col+15, float(l[132:143].strip()), font_style)
        ws.write(row, col+16, float(l[143:154].strip()), font_style)
        ws.write(row, col+17, float(l[154:163].strip()), font_style)
        ws.write(row, col+18, float(l[163:174].strip()), font_style)
        ws.write(row, col+19, float(l[174:185].strip()), font_style)
        ws.write(row, col+20, float(l[185:194].strip()), font_style)
        ws.write(row, col+21, float(l[194:205].strip()), font_style)
        ws.write(row, col+22, float(l[205:215].strip()), font_style)
        ws.write(row, col+23, float(l[215:224].strip()), font_style)
        ws.write(row, col+24, float(l[224:235].strip()), font_style)
        row += 1
    if l[0:8].strip() == '0CATATAN':
        break

wb.save(os.path.join(MFXLS_DIR, filename))