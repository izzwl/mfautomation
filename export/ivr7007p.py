import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR7007P'
filename = args.output if args.output else 'IVR7007P.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','NP#-UM','NIK','NAME','DATE-UM','NP#-PJK','DATE-PJK','BP#','S','DATE-VER','DAYS-P','DAYS-V','MTU','SALDO-PJK','REMARK','NIK-APPR','TGL-APPR'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,6,16,23,39,47,57,66,76,80,87,93,100,106,124,144,153,161
])
export.set_date_col0([4,6,9,16])
export.set_num_col0([10,11,13])
export.export()
