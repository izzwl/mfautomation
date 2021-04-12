import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'MCR2002-RESUME'
filename = args.output if args.output else 'MCR2002-RESUME.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'K-ORG','NIK','NAMA','REKENING','JUMLAH',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,8,15,46,62,73,
])
export.set_date_col0([])
export.set_num_col0([4])
export.export()
