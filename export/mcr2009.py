import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'MCR2009'
filename = args.output if args.output else 'MCR2009.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','NIK','NAMA','ALAMAT 1','ALAMAT 2','ALAMAT 3',
])
export.set_firstlinedata(1)
export.set_popotongan([
    2,8,17,40,80,120,160
])
export.set_date_col0([])
export.set_num_col0([])
export.export()
