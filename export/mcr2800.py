import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'MCR2800'
filename = args.output if args.output else 'MCR2800.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO','ORG','NAMA-ORG','NIK','NAME','KD','NAMA','LAHIR','L/P','STS','UMUR','GRADE'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,5,11,37,44,72,76,98,106,111,116,121,126,
])
export.set_date_col0([7])
export.set_num_col0([])
export.set_text_col0([])
export.export()