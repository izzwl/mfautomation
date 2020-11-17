import argparse
import os
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IAP1500'
filename = args.output if args.output else 'IAP1500.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'SNDI','NAMA-SANDI','JENIS','F-SENTRAL','ANGGARAN-AWAL',
    'REALISASI-ANGGARAN','SUB','PLAFOND-BUDGET','PLAFOND-PR',
    'REALISASI-PR','PLAFOND-PO','REALISASI-PO','ANGGARAN-AKHIR',
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,6,36,49,60,81,105,110,134,158,182,206,230,254,
])
export.set_date_col0([])
export.set_num_col0([4,5,7,8,9,10,11,12])
export.export()
