import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'GAJI-KEKJK'
filename = args.output if args.output else 'GAJI-KEKJK.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'K-ORG','NIK','NAMA','JAM-KERJA','ISTIRAHAT','JML-MENIT'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,7,14,44,50,62,74
])
export.set_date_col0([])
export.set_int_col0([3,4,5])
export.export()
