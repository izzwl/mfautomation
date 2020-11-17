import argparse
import os
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR7050H'
filename = args.output if args.output else 'IVR7050H.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'OWN','PO#','DATE','BYR','NIK','STS','DATE','SANDI','PG','C','P',
    'T','','VENDOR','MTU','NILAI-PO','NILAI-RV','NILAI-DIBAYAR-VCHR',
    'NILAI-DIBAYAR-KU','NILAI-SISA(RV-KU)','P','I','O','SBU',
    'NILAI-NP/BA',
])
export.set_firstlinedata(4)
export.set_popotongan([
    1,5,14,22,26,33,37,45,51,54,56,59,60,66,89,93,111,129,147,165,184,186,188,
    190,194,213
])
export.set_date_col0([2,6])
export.set_num_col0([15,16,17,18,19,24])
export.export()
