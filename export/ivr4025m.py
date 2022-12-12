import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR4025M'
filename = args.output if args.output else 'IVR4025M.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'WOM#','WIP#','PART-NUMBER','DESCRIPTION','OWN','N','D','C','AREA','REQ#',
    'AUT-DTE','REQ-BY','REQ-QTY','UM','ISS-DTE','RETURN','PRICE-USD','EXT-PRICE-USD',
    'IPOKEY','NAMA-VENDOR','FROM-BIN#','TAG#','WOM#','RV#','RECEIVED-ISSUED',
    'QPA','PR#','STS','INV-STOCK','ROT-STOCK','F','PO#','ITEM','TOP',
    'RECEIVED-PR','ACCEPTED','STORED','ESN','PR-CONSIG'
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,8,16,37,73,77,79,81,83,88,99,107,122,130,133,141,147,160,175,187,216,
    227,234,241,250,268,272,281,284,294,304,307,316,321,325,337,346,355,376,400
])
export.set_date_col0([10,34,35,36])
export.set_num_col0([12,16,17,28,29])
export.export()
