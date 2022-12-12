import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR2080A'
filename = args.output if args.output else 'IVR2080A.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','NHA-P/N','METAG','IPC-NUMBER','PART-NUMBER','DESCRIPTION',
    'QPA','CCL','MCL','FPI','MPI','INS'
])
export.set_firstlinedata(1)
export.set_popotongan([
    1,7,29,35,51,73,91,96,112,128,144,160,167
])
export.set_date_col0([])
export.set_num_col0([])
export.export()
