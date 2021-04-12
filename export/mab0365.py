import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'MAB0365'
filename = args.output if args.output else 'MAB0365.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'WOM#','TMWO#','CREATED','S','','TYPE#','PART#','SER#','OWN','TYP',
    'QTY','EMPLNO','TSK','DESCRIPTION','SHOP','','STATUS','START','','','COMPLETE','','','LT','M/H'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,8,16,24,26,30,37,58,74,78,82,86,94,98,147,151,154,167,175,
    178,182,190,193,196,203,210,
])
export.set_date_col0([2,17,20])
export.set_num_col0([18,19,21,22,23,24])
export.set_text_col0([])
export.export()
