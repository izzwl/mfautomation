import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'LDB0103B'
filename = args.output if args.output else 'LDB0103B.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO','NIK','NAMA','DWC/CATAT',' ','AVAILABLE-HOURS','JAM-KERJA-DU',
    'CAJ-HOURS-REGULER','CAJ-HOURS-OVERTIME','TOTAL',
    'WIP-HOURS-REGULER','WIP-HOURS-OVERTIME','TOTAL',
    '%DARI-AVAILABLE','%DARI-JK(DU)','KD-ORG',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,6,13,30,35,38,47,56,66,77,85,95,105,114,123,131,
])
export.set_date_col0([])
export.set_num_col0([3,4,5,6,7,8,9,10,11,12,13,14])
export.export()
