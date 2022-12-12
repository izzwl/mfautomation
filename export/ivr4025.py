import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR4025'
filename = args.output if args.output else 'IVR4025.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'WOM#','TMWO#','PART-NUMBER','DESCRIPTION','OWN','COND','DISP',
    'PRT-CD','QPA','#','REQ#','REQ-BY','QTY','UM','ISSUED','RETURN',
    'PRICE-USD','EXT-USD','PRICE-AVG-RPH','EXT-AVG-RPH',
    'PRICE-AVG-USD','EXT-AVG-USD','PRICE-LIST','TH','PO#-ISSUED',
    'NAMA-VENDOR','PR#-BND','MTCD','PO#-BND','ITEM','RECEIVED',
    'ACCEPTED','STORED','D/F','PR-CONSIG'
])
export.set_firstlinedata(1)
export.set_popotongan([
    1,8,16,37,73,77,82,87,94,98,100,110,125,132,136,144,150,163,179,
    194,210,224,238,251,255,267,298,307,312,321,326,335,344,353,357,
    400
])
export.set_date_col0([14,30,31,32])
export.set_num_col0([12,16,17,18,19,20,21,22])
export.export()
