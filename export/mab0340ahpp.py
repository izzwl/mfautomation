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
filename = args.output if args.output else 'MAB0340A-HPP.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'WIP-WOM','X','JML-MH','MAT-IN-RPH','MH-IN-RPH','MAT-AVG-USD','MH-IN-USD','PG','CUS','P','S','RST','SERIAL#','PENYESUAIAN-USD','MAT-IN-USD','OPENED','MESIN-USD'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,8,11,20,39,58,77,90,94,98,100,102,106,126,143,158,166,181,
])
export.set_date_col0([15])
export.set_num_col0([2,3,4,5,6,11,13,14,16])
export.set_text_col0([])
export.export()
