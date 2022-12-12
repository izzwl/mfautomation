import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'VRP1500'
filename = args.output if args.output else 'VRP1500.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'WIP#','P','PART#/PO#','SERIAL-NUMB','QTY','REST','TYPE-NUMB','CUS','OPENED','RECEIVE','WIP-STATUS','PG','MS-NUMB','S','MS-DATE','TRT-A','TRT-P','W-TERMIN','REMARK','SBU','NAMA-CUSTOMER','D/F'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,8,10,32,54,59,64,75,80,88,97,112,116,126,128,135,141,147,159,360,366,397,400,
])
export.set_date_col0([8,9,14,])
export.set_num_col0([])
export.set_text_col0([])
export.export()
