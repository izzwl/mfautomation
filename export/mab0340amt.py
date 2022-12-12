import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'MAB0340A'
filename = args.output if args.output else 'MAB0340A-MT.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'WOM','TMWO','BND#','ISSUED','PART-NUMBER','QTY','RTURN','AVG-PRICE','AVG-PRICE-USD'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,8,15,25,32,53,59,65,79,92,
])
export.set_date_col0([3])
export.set_num_col0([5,6,7,8])
export.set_text_col0([])
export.export()
