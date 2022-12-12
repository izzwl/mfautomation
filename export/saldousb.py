import argparse
import os,sys,re
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
# parser.add_argument('--periode', help='210101 210131')
args = parser.parse_args()

outlist = args.input if args.input else 'SALDOUSB'
filename = args.output if args.output else 'SALDOUSB.xls'
export = xlsExport(outlist,filename)
font_style = export.font_header_style


#sheet SALDOUSB
export.ws = export.wb.add_sheet('NON-UMC')
export.ws.write_merge(0,1,0,0,'NO', font_style)
export.ws.write_merge(0,1,1,1,'PGM', font_style)
export.ws.write_merge(0,1,2,2,'NO.WIP', font_style)
export.ws.write_merge(0,1,3,3,'SERIAL#', font_style)
export.ws.write_merge(0,1,4,4,'CUST', font_style)
export.ws.write_merge(0,1,5,5,'START', font_style)
export.ws.write_merge(0,1,6,6,'ECD', font_style)
export.ws.write_merge(0,1,7,7,'CUR', font_style)
export.ws.write_merge(0,1,8,8,'NILAI-PENJUALAN-USD', font_style)
export.ws.write_merge(0,0,9,12,'ANGGARAN-USD', font_style)
export.ws.write(1,9,'MATERIAL', font_style)
export.ws.write(1,10,'MANHOUR', font_style)
export.ws.write(1,11,'OTHER', font_style)
export.ws.write(1,12,'TOTAL', font_style)
export.ws.write_merge(0,1,13,13,'PROFIT-MARGIN(%)', font_style)
export.ws.write_merge(0,0,14,21,'REALISASI-USD', font_style)
export.ws.write(1,14,'MATERIAL', font_style)
export.ws.write(1,15,'%', font_style)
export.ws.write(1,16,'MANHOUR', font_style)
export.ws.write(1,17,'%', font_style)
export.ws.write(1,18,'OTHER', font_style)
export.ws.write(1,19,'%', font_style)
export.ws.write(1,20,'TOTAL', font_style)
export.ws.write(1,21,'%', font_style)
export.ws.write_merge(0,1,22,22,'PROSES', font_style)
export.ws.write_merge(0,1,23,23,'AKUM', font_style)
export.ws.write_merge(0,1,24,24,'S', font_style)
export.ws.write_merge(0,1,25,25,'CREATED', font_style)
export.ws.write_merge(0,1,26,26,'NAMA', font_style)
export.ws.write_merge(0,1,27,27,'DESCRIPTION', font_style)
export.ws.write_merge(0,1,28,28,'SBU', font_style)
export.ws.write_merge(0,1,29,29,'CUR=VP40(Y/N)', font_style)
export.ws.write_merge(0,1,30,30,'KURS USD', font_style)
export.ws.write_merge(0,1,31,31,'TOTAL QUOTATION', font_style)
export.ws.write_merge(0,1,32,32,'MOS#', font_style)
export.ws.write_merge(0,1,33,33,'CREATED', font_style)
export.ws.write_merge(0,1,34,34,'PENYESUAIAN', font_style)
export.ws.write_merge(0,1,35,35,'P', font_style)
export.ws.write_merge(0,1,36,36,'X', font_style)
export.ws.write_merge(0,1,37,37,'KD-PT-DI', font_style)
export.ws.write_merge(0,1,38,38,'NAMA-CUSTOMER', font_style)
export.ws.write_merge(0,1,39,39,'MTU', font_style)
export.ws.write_merge(0,1,40,40,'TOTAL-INVOICE', font_style)
export.ws.write_merge(0,1,41,41,'TOTAL-PAYMENT', font_style)
export.ws.write_merge(0,1,42,42,'TOTAL-INVOICE-USD', font_style)
export.ws.write_merge(0,1,43,43,'TOTAL-PAYMENT-USD', font_style)
export.first_line_regex_offset = 3
export.first_line_regex ="^.*SALDO WIP \(NON-UMC\)"
export.end_line_regex = None
export.set_popotongan([
    1,5,9,16,37,42,51,60,64,84,105,126,147,168,185,207,217,236,246,265,276,295,306,313,318,321,328,359,380,385,399,407,425,437,445,463,465,467,477,507,512,530,548,567,586
])
export.set_num_col0([8,9,10,11,12,13,14,15,16,17,18,19,20,21,30,31,34,41,42,43,44])
export.set_int_col0([])
export.set_date_col0([5,6])
export.get_raw_lines()
export.write_body(row=2)
export.auto_width()
export.save_export()
exit()

