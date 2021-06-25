import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR1327'
filename = args.output if args.output else 'IVR1327.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'REQ-NUMBER','REQUESTED-DATE','PART-NUMBER','PART-DESCRIPTION',
    'ISSU/REQ','UOM','ISSUED-DATE','WOM/OR','CUST','DURASI/HR','S'
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,12,27,48,83,93,97,109,116,120,131,133
])
export.set_date_col0([1,6])
export.set_num_col0([4])
export.export()
