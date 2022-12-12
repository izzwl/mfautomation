import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR9100'
filename = args.output if args.output else 'IVR9100.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'EMPLNO#','EXP-DATE','NAMA','KD-ORG','JOB-CD','JOB-TITLE','PP','TR','EXP-DATE','KD','TGL-LAHIR',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,10,20,52,60,68,99,108,117,126,131,140,
])
export.set_date_col0([1,10])
export.set_num_col0([])
export.export()
