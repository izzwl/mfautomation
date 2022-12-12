import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'LDB0103A'
filename = args.output if args.output else 'LDB0103A.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NIK','NAMA','GR','ORG','NAMA-ORG','TGL','KD','J-DAT','J-PUL','LDAT','LPUL',
    'LTOT','LIBUR','LBH-T','LBH-L','ATH'
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,8,39,42,48,74,82,85,91,97,102,107,112,118,124,130,132
])
export.set_date_col0([5])
export.set_num_col0([])
export.export()
