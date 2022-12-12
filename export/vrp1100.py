import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'VRP1100'
filename = args.output if args.output else 'VRP1100.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'PG','CUS','PO-NUMBER','WO-NUMBR','WIP#','CREATD','W','T','P','C','JOB',
    'PART-NUMBER','SERIAL-NUMBER','TYPE-NUMBR',' ','TYPE-DESCRIPTION',
    'RECEIVED','OPENED','CLOSED','START','DAYS','E.C.D','Q-REST','T',
    'TARGET','REMARK','X','TOT-QUOTATION','QTY','MAT-QUOTATION',
    'M/H-QUOTATION','OTH-QUOTATION','SBU','NAMA-CUSTOMER','MTU',
    'CUR=VP40','FINAL-QUOT'
])
export.set_firstlinedata(4)
export.set_popotongan([
    1,4,8,29,38,45,52,54,56,58,60,64,85,106,110,117,138,147,155,163,171,176,
    184,190,193,202,263,265,281,284,302,319,336,342,373,377,386,402
])
export.set_date_col0([16,17,18,19,21])
export.set_num_col0([27,28,29,30,31,36])
export.export()
