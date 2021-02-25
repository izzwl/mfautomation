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
outlist = os.path.join(MFOUTLIST_DIR,'%s'%(args.input if args.input else 'IAP1100' ))
filename = "%s.xls"%(args.output if args.output else 'IAP1100' )

wb = xlwt.Workbook(encoding='utf-8',style_compression=2)
ws = wb.add_sheet('Sheet 1')
# Sheet header, first row
row_num = 0

font_style = xlwt.XFStyle()
font_header_style = xlwt.easyxf('font: bold true; borders: left thin, right thin, top thin, bottom thin;')
font_body_style = xlwt.easyxf('borders: left thin, right thin, bottom thin;')
# font_style.font.bold = True
header = [
    'NO.','VOUCHER#','VOID','JNS','CREATED','NOTA#','DATE','SANDI',
    'NILAI-NOTA','URAIAN','REF-NOTA','NO-BAYAR','TANGGAL','INVOICE#',
    'DATE','SNDI','PG','WOM#','ORG','SBU','NIK/VENDOR','PJK','KDORG',
    'MTU','NILAI-VOUCHER','T-KURS','NILAI-VOUCHER-RPH','NILAI-PPH','S',
    'NILAI-PPN','S','SALDO-PJK','TERIMA','UMUR','VENDOR-BANK','PRINTED',
    'VOIDED','KH','DUE-DATE-NP','DUE-DATE-VCR','NO-PPN','NO-PPH'
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
        ws.write(row, col+0, l[1:6].strip(), font_style)
        ws.write(row, col+1, l[6:16].strip(), font_style)
        ws.write(row, col+2, l[16:21].strip(), font_style)
        ws.write(row, col+3, l[21:25].strip(), font_style)
        ws.write(row, col+4, l[25:33].strip(), font_style)
        ws.write(row, col+5, l[33:43].strip(), font_style)
        ws.write(row, col+6, l[43:51].strip(), font_style)
        ws.write(row, col+7, l[51:56].strip(), font_style)
        ws.write(row, col+8, l[56:76].strip(), font_style)
        ws.write(row, col+9, l[76:127].strip(), font_style)
        ws.write(row, col+10, l[127:137].strip(), font_style)
        ws.write(row, col+11, l[137:148].strip(), font_style)
        ws.write(row, col+12, l[148:156].strip(), font_style)
        ws.write(row, col+13, l[156:177].strip(), font_style)
        ws.write(row, col+14, l[177:185].strip(), font_style)
        ws.write(row, col+15, l[185:190].strip(), font_style)
        ws.write(row, col+16, l[190:193].strip(), font_style)
        ws.write(row, col+17, l[193:200].strip(), font_style)
        ws.write(row, col+18, l[200:207].strip(), font_style)
        ws.write(row, col+19, l[207:212].strip(), font_style)
        ws.write(row, col+20, l[212:234].strip(), font_style)
        ws.write(row, col+21, l[234:238].strip(), font_style)
        ws.write(row, col+22, l[238:244].strip(), font_style)
        ws.write(row, col+23, l[244:247].strip(), font_style)
        ws.write(row, col+24, l[247:267].strip(), font_style)
        ws.write(row, col+25, l[267:274].strip(), font_style)
        ws.write(row, col+26, l[274:293].strip(), font_style)
        ws.write(row, col+27, l[293:310].strip(), font_style)
        ws.write(row, col+28, l[310:313].strip(), font_style)
        ws.write(row, col+29, l[313:330].strip(), font_style)
        ws.write(row, col+30, l[330:333].strip(), font_style)
        ws.write(row, col+31, l[333:351].strip(), font_style)
        ws.write(row, col+32, l[351:361].strip(), font_style)
        ws.write(row, col+33, l[361:367].strip(), font_style)
        ws.write(row, col+34, l[367:483].strip(), font_style)
        ws.write(row, col+35, l[483:491].strip(), font_style)
        ws.write(row, col+36, l[491:499].strip(), font_style)
        ws.write(row, col+37, l[499:502].strip(), font_style)
        ws.write(row, col+38, l[502:514].strip(), font_style)
        ws.write(row, col+39, l[514:530].strip(), font_style)
        ws.write(row, col+40, l[530:541].strip(), font_style)
        ws.write(row, col+41, l[541:].strip(), font_style)
        row += 1

wb.save(os.path.join(MFXLS_DIR, filename))