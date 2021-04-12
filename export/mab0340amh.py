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
filename = args.output if args.output else 'MAB0340A-MH.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'WOM','TMWO','TGL','NIK','MENIT','MESIN','RATE-USD','HPK',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,8,15,22,29,33,38,48,52,
])
export.set_date_col0([2])
export.set_num_col0([4,6,7])
export.set_text_col0([])
export.export()
