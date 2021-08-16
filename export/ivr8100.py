import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR8100'
filename = args.output if args.output else 'IVR8100.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','MATERIAL CLASS','EMP.NO.','DATE',''
])
export.set_firstlinedata(0)
export.set_popotongan([
    2,11,37,50,58,62
])
export.set_date_col0([])
export.set_num_col0([])
export.export()
