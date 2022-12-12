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
outlist = os.path.join(MFOUTLIST_DIR,'%s'%(args.input if args.input else 'MCR2008' ))
filename = "%s.xls"%(args.output if args.output else 'MCR2008' )

wb = xlwt.Workbook(encoding='utf-8',style_compression=2)
ws = wb.add_sheet('Sheet 1')
# Sheet header, first row
row_num = 0

font_style = xlwt.XFStyle()
font_header_style = xlwt.easyxf('font: bold true; borders: left thin, right thin, top thin, bottom thin;')
font_body_style = xlwt.easyxf('borders: left thin, right thin, bottom thin;')
# font_style.font.bold = True
header = [
    'NO.','KDORG','DESCRIPTION','NIK','NAMA','JOB-CD',' ','RUMPUN',
    'JOB-TITLE','STS-JOB','JENIS','TMT','GR','IN','F','J','S','J','H',
    'P',' ','DESCRIPTION','K','A','GL','MK','M','C','LAHIR','TMT-UMC',
    'TMTKGG','TMT-CB','TM'
]
for col_num in range(len(header)):
    ws.write(row_num, col_num, header[col_num], font_header_style)

no = 0
row = 1

f = open(outlist, "r")
s = 0
lines = f.readlines()
for i,l in enumerate(lines):
    if i > 4:
        col = 0
        ws.write(row, col+0, l[1:5].strip(), font_style)
        ws.write(row, col+1, l[5:12].strip(), font_style)
        ws.write(row, col+2, l[12:38].strip(), font_style)
        ws.write(row, col+3, l[38:45].strip(), font_style)
        ws.write(row, col+4, l[45:76].strip(), font_style)
        ws.write(row, col+5, l[76:83].strip(), font_style)
        ws.write(row, col+6, l[83:86].strip(), font_style)
        ws.write(row, col+7, l[86:107].strip(), font_style)
        ws.write(row, col+8, l[107:138].strip(), font_style)
        ws.write(row, col+9, l[138:146].strip(), font_style)
        ws.write(row, col+10, l[146:153].strip(), font_style)
        ws.write(row, col+11, l[153:161].strip(), font_style)
        ws.write(row, col+12, l[161:164].strip(), font_style)
        ws.write(row, col+13, l[164:167].strip(), font_style)
        ws.write(row, col+14, l[167:169].strip(), font_style)
        ws.write(row, col+15, l[169:171].strip(), font_style)
        ws.write(row, col+16, l[171:173].strip(), font_style)
        ws.write(row, col+17, l[173:175].strip(), font_style)
        ws.write(row, col+18, l[175:177].strip(), font_style)
        ws.write(row, col+19, l[177:180].strip(), font_style)
        ws.write(row, col+20, l[180:184].strip(), font_style)
        ws.write(row, col+21, l[184:201].strip(), font_style)
        ws.write(row, col+22, l[201:203].strip(), font_style)
        ws.write(row, col+23, l[203:205].strip(), font_style)
        ws.write(row, col+24, l[205:208].strip(), font_style)
        ws.write(row, col+25, l[208:211].strip(), font_style)
        ws.write(row, col+26, l[211:213].strip(), font_style)
        ws.write(row, col+27, l[213:216].strip(), font_style)
        ws.write(row, col+28, l[216:224].strip(), font_style)
        ws.write(row, col+29, l[224:232].strip(), font_style)
        ws.write(row, col+30, l[232:240].strip(), font_style)
        ws.write(row, col+31, l[240:248].strip(), font_style)
        ws.write(row, col+32, l[248:250].strip(), font_style)
        row += 1

wb.save(os.path.join(MFXLS_DIR, filename))