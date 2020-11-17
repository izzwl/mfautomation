import argparse
import datetime
import os
import xlwt
import decimal

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

MFOUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')
MFXLS_DIR = os.path.join(os.path.expanduser("~"),'mfxls')
outlist = os.path.join(MFOUTLIST_DIR,'%s'%(args.input if args.input else 'IAP1200' ))
filename = "%s.xls"%(args.output if args.output else 'IAP1200' )

wb = xlwt.Workbook(encoding='utf-8',style_compression=2)
ws = wb.add_sheet('Sheet 1')
# Sheet header, first row
row_num = 0

font_style = xlwt.XFStyle()
font_header_style = xlwt.easyxf('font: bold true; borders: left thin, right thin, top thin, bottom thin;')
font_body_style = xlwt.easyxf('borders: left thin, right thin, bottom thin;')
# font_style.font.bold = True
header = [
    'NOTA#',
    'JNS',
    'STS',
    'CREATED',
    'NIK-NOTA',
    'MTU',
    'NILAI-NOTA',
    'VEND/NIK',
    'NAMA',
    'SNDI',
    'PG',
    'WOM#',
    'ORG',
    'SBU',
    'NILAI-NOTA-RPH',
    'VOUCHER#',
    'DATE',
    'BAYAR#',
    'DATE',
    'URAIAN',
    'NO-REFERENSI',
    'KH',
    'SALDO-PJK',
    'SALDO-PJK-BM',
]
for col_num in range(len(header)):
    ws.write(row_num, col_num, header[col_num], font_header_style)
popotongan = [
    1,10,13,18,25,34,39,57,67,88,93,97,104,111,114,132,142,150,161,
    169,220,241,243,261,279
]
date_col0 = [
    3,16,18,
]

date_style = xlwt.easyxf(num_format_str="D-MMM-YY")
num_col0 = [
    4,14,22,23
]
num_style = xlwt.easyxf(num_format_str="#,##0.00")
no = 0
row = 1
f = open(outlist, "r")
s = 0
lines = f.readlines()
for i,l in enumerate(lines):
    if i > 3:
        for col,p in enumerate(popotongan):
            if col < len(popotongan) - 1:
                style = font_style
                data = l[p:popotongan[col+1]].strip()
                if col in date_col0:
                    data = datetime.datetime.strptime(data,"%d%b%y") if data else ''
                    style = date_style
                if col in num_col0:
                    data = decimal.Decimal(data.replace(',','')) 
                    style = num_style
                ws.write(row, col, data ,style) 
        row += 1
        # ws.write(row, col+0, l[1:10].strip(), font_style)
        # ws.write(row, col+1, l[10:13].strip(), font_style)
        # ws.write(row, col+2, l[13:18].strip(), font_style)
        # ws.write(row, col+3, l[18:25].strip(), font_style)
        # ws.write(row, col+4, l[25:34].strip(), font_style)
        # ws.write(row, col+5, l[34:39].strip(), font_style)
        # ws.write(row, col+6, l[39:57].strip(), font_style)
        # ws.write(row, col+7, l[57:67].strip(), font_style)
        # ws.write(row, col+8, l[67:88].strip(), font_style)
        # ws.write(row, col+9, l[88:93].strip(), font_style)
        # ws.write(row, col+10, l[93:97].strip(), font_style)
        # ws.write(row, col+11, l[97:104].strip(), font_style)
        # ws.write(row, col+12, l[104:111].strip(), font_style)
        # ws.write(row, col+13, l[111:114].strip(), font_style)
        # ws.write(row, col+14, l[114:132].strip(), font_style)
        # ws.write(row, col+15, l[132:142].strip(), font_style)
        # ws.write(row, col+16, l[142:150].strip(), font_style)
        # ws.write(row, col+17, l[150:161].strip(), font_style)
        # ws.write(row, col+18, l[161:169].strip(), font_style)
        # ws.write(row, col+19, l[169:220].strip(), font_style)
        # ws.write(row, col+20, l[220:241].strip(), font_style)
        # ws.write(row, col+21, l[241:243].strip(), font_style)
        # ws.write(row, col+22, l[243:261].strip(), font_style)
        # ws.write(row, col+23, l[261:279].strip(), font_style)

wb.save(os.path.join(MFXLS_DIR, filename))