import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR7050U'
filename = args.output if args.output else 'IVR7050U.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'MATERIAL-CLASS','PART-NUMBER','C','DESCRIPTION','USE-CODE(APPLY)','BIN#',
    'STORE','OWN','QTY','UM','EXT-PRICE-USD','EXT-PRICE-RPH','RV/MR#','WIP','WOM',
    'ISS-BND','RV#-BND','INVOICE#','PACKING-LIST#','S','DATE-7','CUST','SERIAL#',
    'REQ#','REQ-BY','RECEIVED','PR#','PO#','EXP-CD','REFERENCE','DAP','BRIS'
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,22,43,45,62,83,94,101,104,113,116,129,144,153,162,169,177,186,207,228,
    230,238,243,264,274,290,299,308,317,324,345,349,358
])
export.set_date_col0([15,20,25])
export.set_num_col0([8,10,11])
export.export()
