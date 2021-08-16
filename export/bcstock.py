import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'BCSTOCK'
filename = args.output if args.output else 'BCSTOCK.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'KODE-BARANG','KODE-HS','URAIAN-BARANG','JENIS-BARANG','TIPE','SATUAN','STOCK-AKHIR','BIN#','RV#'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,22,33,69,82,87,93,105,117,125
])
export.set_date_col0([])
export.set_num_col0([6])
export.export()
