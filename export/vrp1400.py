import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'VRP1400'
filename = args.output if args.output else 'VRP1400.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','MS#','S','CREATED','CODE','CUSTOMER','WO#','PO#','WIP#','S','','TYPE#','MS-QTY','CRE-BY','SBU',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,6,15,17,25,29,60,69,90,97,99,103,109,116,123,127
])
export.set_date_col0([3])
export.set_num_col0([])
export.set_text_col0([7,8,11])
export.export()
