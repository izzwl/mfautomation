import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR7020H'
filename = args.output if args.output else 'IVR7020H.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','MASTER#','PO#','CREATED','BYR','S','SANDI','PG','F','P','C',
    'PT','PI','PJK','ITM','PR#','WOM#','SANDI','PART-NUMBER',
    'DESCRIPTION','DUE-DATE','QTY','','MTU','UNIT-PRICE',
    'EXT-PRICE(RPH)','VENDOR','F','SO','SR','TEXT','HS#',
    'RECEIVED','INSPECTED','STORED','PO-STS-3','C','P',
    'DOKUMEN','ENG-DISP','LIFE-TIME','COUNTRY'
])
export.set_firstlinedata(1)
export.set_popotongan([
    1,6,15,30,38,42,44,50,53,55,57,59,62,65,69,73,83,90,96,117,138,146,156,160,163,178,193,216,218,221,224,575,586,595,
    605,614,623,625,627,637,646,656,700
])
export.set_date_col0([3,20,32,33,34,35])
export.set_num_col0([21,24,25])
export.export()
