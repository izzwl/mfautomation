import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'BEACUKAI'
filename = args.output if args.output else 'BEACUKAI.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'WOM#','WIP#','PART-NUMBER','DESCRIPTION','HS-NUMBER','BM(%)','OWN',
    'REQ#','ISSUE-QTY','','ISS-DTE','PRICE-USD','IPOKEY','RV#','D/F','B',
    'BPBI/BPBL','RECEIVED','NA','TGL-BC23','NOMOR-PENGAJUAN','TGL-AJU','PRICE-AVG-USD'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,8,16,37,73,88,95,100,109,118,121,128,141,152,161,165,167,188,
    198,201,210,237,244,259
])
export.set_date_col0([10,17,19,21])
export.set_num_col0([5,8,11,22])
export.export()
