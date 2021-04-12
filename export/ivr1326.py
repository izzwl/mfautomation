import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR1326'
filename = args.output if args.output else 'IVR1326.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'REQ-NUMBER','DATE','REQ-BY','AUTH-BY','PART-NUMBER','C',
    'DESCRIPTION','REQ-QTY','UOM','RESV-QTY','STOCK-QTY','UOM','PR-QTY',
    'BLNC-PO','MAT-CLASS','WIP#','WOM#','NEW-PRICE-AVG',
    'EXT-PRICE-AVG','PR#','PRINTED','PO#','PRINTED','NEED-DTE',
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,12,20,27,35,53,55,70,77,79,88,97,100,108,116,131,138,144,159,174,184,193,202,211,219,
])
export.set_date_col0([1,20,22,23])
export.set_num_col0([7,9,10,12,13,17,18])
export.export()
