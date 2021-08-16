import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'BCIN72'
filename = args.output if args.output else 'BCIN72.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'RECEIVED','CREATED','BY','NOMOR-BC','TGL-BC','NO-SJ','TGL-SJ','NOMOR-AJU','TGL-AJU','VENDOR','PO#','ITEM#','PART#','DESCRIPTION','Q-SHIP','Q-RECVD','UM','UNIT-PRICE','CUR'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,10,19,27,49,58,80,89,117,126,158,168,174,196,232,242,252,256,274,279])
export.set_date_col0([0,1,4,6,8])
export.set_num_col0([14,15,17])
export.export()
