import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'TMWO04A'
filename = args.output if args.output else 'TMWO04A.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'WIPNO','TOP','TYPE-NO','PART-NUMBER','TYPE-DESCRIPTION','ALTRN','DC',
    'AQTY','OWN','CHRGE#','OPEN','CLOSE','S','NHAWIP','SERIAL-NO','MAN-HOUR',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,8,12,23,40,58,65,68,73,77,84,92,100,102,109,125,
])
export.set_date_col0([10,11])
export.set_num_col0([15])
export.export()
