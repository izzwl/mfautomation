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
outlist = os.path.join(MFOUTLIST_DIR,'%s'%(args.input if args.input else 'IVR7030E' ))
filename = "%s.xls"%(args.output if args.output else 'IVR7030E' )

wb = xlwt.Workbook(encoding='utf-8',style_compression=2)
ws = wb.add_sheet('Sheet 1')
# Sheet header, first row
row_num = 0

font_style = xlwt.XFStyle()
font_header_style = xlwt.easyxf('font: bold true; borders: left thin, right thin, top thin, bottom thin;')
font_body_style = xlwt.easyxf('borders: left thin, right thin, bottom thin;')
# font_style.font.bold = True
header = [
    'PR#',
    'DATE',
    'S',
    'WOM#',
    'PG',
    'PART#',
    'DESCRIPTION',
    'STS-3',
    'PO#',
    'DATE',
    'S',
    'ITEM',
    'MTU',
    'UNIT-PRICE(PO)',
    'EXT-PRICE(PO)',
    'VENDOR',
    'VENDOR-NAME',
    'NEEDED',
    'PR-QTY',
    'PROMISED',
    'DAYS-LATE',
    'PO-QTY',
    'ACC-QTY',
    'BALANCE',
    'NEW-STOCK',
    'OHC-STOCK',
    'ALT-NEW-STOCK',
    'ALT-OHC-STOCK',
    'SANDI',
    'EXP-CD',
    'UNIT-PRICE(PR)',
    'EXT-PRICE(PR)',
    'MTU',
    'SERIAL#',
    'EXT-PRICE-REQ(RPH)',
    'STATUS-TERAKHIR',
    'SBU',
    'GPR#',
    'F',
    'BYR-M',
    'BYR-P',
    'OWN',
    'MTCD',
    'COND',
    'ACCEPTED',
    'STS-DATE',
    'RFQ#',
    'DATE',
    'BYR',
    'CREATE',
    'PRINT',
    'FINANCE',
    'APPROVE',
    'RFQ',
    'OA',
    'PO',
    'REQ#/ORG',
    'AUTH/NEW-BND',
    'CUST',
    'C',
]
for col_num in range(len(header)):
    ws.write(row_num, col_num, header[col_num], font_header_style)

popotongan = [
    1,11,19,21,28,31,52,88,96,106,114,116,121,124,140,156,164,195,
    202,212,221,231,243,254,265,276,287,302,317,324,330,348,365,370,
    390,409,491,495,500,502,508,514,518,523,528,537,546,555,563,567,
    577,587,597,607,617,627,637,647,660,665
]
date_col0 = [
    1,7,9,17,19,44,45,47,49,50,51,52,53,54,55,57
]

date_style = xlwt.easyxf(num_format_str="D-MMM-YY")
num_col0 = [
    13,14,18,21,22,23,24,25,26,27,30,31,34,
]
num_style = xlwt.easyxf(num_format_str="#,##0.00")

no = 0
row = 1
f = open(outlist, "r")
s = 0
lines = f.readlines()
for i,l in enumerate(lines):
    if i > 5:
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

wb.save(os.path.join(MFXLS_DIR, filename))