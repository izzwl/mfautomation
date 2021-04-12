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
outlist = os.path.join(MFOUTLIST_DIR,'%s'%(args.input if args.input else 'PPB1300A' ))
filename = "%s.xls"%(args.output if args.output else 'PPB1300A' )

wb = xlwt.Workbook(encoding='utf-8',style_compression=2)
ws = wb.add_sheet('Sheet 1')
# Sheet header, first row
row_num = 0

font_style = xlwt.XFStyle()
font_header_style = xlwt.easyxf('font: bold true; borders: left thin, right thin, top thin, bottom thin;')
font_body_style = xlwt.easyxf('borders: left thin, right thin, bottom thin;')
# font_style.font.bold = True
header = [
    'PPCL#','METTAG','PART-NUMBER-OFF','DESCRIPTION-OFF','STS','N-STS','Q-OFF',
    'SERIAL#-OFF','TRANSFER-TO','PART-NUMBER-ON','DESCRIPTION-ON','Q-ON',
    'SERIAL#-ON','FROM','BND/TG#/LAIN','REASON1','REASON2','REASON3','TAGNO',
    'FD-TAG','QPA','TRANSF-DATE','TMWO#','INV-STOCK','ROT-STOCK','ALT-STOCK',
    'ALT-ROT','REQ#-TAG','REQ#-ON','CONDITION',
]
for col_num in range(len(header)):
    ws.write(row_num, col_num, header[col_num], font_header_style)

no = 0
row = 1

f = open(outlist, "r")
s = 0
lines = f.readlines()
for i,l in enumerate(lines):
    if i > 6:
        col = 0
        ws.write(row, col+0, l[1:14].strip(), font_style)
        # ws.write(row, col+0, l[1:3].strip(), font_style)
        # ws.write(row, col+1, l[3:10].strip(), font_style)
        # ws.write(row, col+2, l[10:14].strip(), font_style)
        ws.write(row, col+1, l[14:22].strip(), font_style)
        ws.write(row, col+2, l[22:44].strip(), font_style)
        ws.write(row, col+3, l[44:81].strip(), font_style)
        ws.write(row, col+4, l[81:87].strip(), font_style)
        ws.write(row, col+5, l[87:93].strip(), font_style)
        ws.write(row, col+6, l[93:99].strip(), font_style)
        ws.write(row, col+7, l[99:117].strip(), font_style)
        ws.write(row, col+8, l[117:129].strip(), font_style)
        ws.write(row, col+9, l[129:150].strip(), font_style)
        ws.write(row, col+10, l[150:187].strip(), font_style)
        ws.write(row, col+11, l[187:193].strip(), font_style)
        ws.write(row, col+12, l[193:210].strip(), font_style)
        ws.write(row, col+13, l[210:222].strip(), font_style)
        ws.write(row, col+14, l[222:241].strip(), font_style)
        ws.write(row, col+15, l[241:312].strip(), font_style)
        ws.write(row, col+16, l[312:383].strip(), font_style)
        ws.write(row, col+17, l[383:454].strip(), font_style)
        ws.write(row, col+18, l[454:464].strip(), font_style)
        ws.write(row, col+19, l[464:474].strip(), font_style)
        ws.write(row, col+20, l[474:478].strip(), font_style)
        ws.write(row, col+21, l[478:490].strip(), font_style)
        ws.write(row, col+22, l[490:498].strip(), font_style)
        ws.write(row, col+23, l[498:508].strip(), font_style)
        ws.write(row, col+24, l[508:518].strip(), font_style)
        ws.write(row, col+25, l[518:528].strip(), font_style)
        ws.write(row, col+26, l[528:538].strip(), font_style)
        ws.write(row, col+27, l[538:548].strip(), font_style)
        ws.write(row, col+28, l[548:558].strip(), font_style)
        ws.write(row, col+29, l[558:].strip(), font_style)
        row += 1

wb.save(os.path.join(MFXLS_DIR, filename))