import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'VRP1100K'
filename = args.output if args.output else 'VRP1100K.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'PG','CUS','PO-NUMBER','WO-NUMBR','WIP#','CREATD','W','T','P','C','JOB','PART-NUMBER','SERIAL-NUMBER','TYPE-NUMBR','TYPE-DESCRIPTION','Q-REST','MS-NUMB','MS-DATE','QTY','INVOICE#','BILL','MTU','NILAI-INVOICE','PAYMENT#','NILAI-PAYMENT','TOTAL-MH-HPP-RPH','TOTAL-MAT-HPP-RPH','TOTAL-MH-HPP-USD','TOTAL-MAT-HPP-USD','PO-DATE','OPEN/AMEND0','RECEIVE/INSPECTION','START/INDUCTION','FINAL-DISPO','QUOTATION','QUOT-CONF','BILLING','INVOICE','PAYMENT','CLOSED','X','TSN','TSO','CNS','CSO','CUST-NAME','REMARK','SBU','ECD',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,4,8,29,38,45,52,54,56,58,60,64,85,106,117,138,145,155,163,167,176,181,185,205,215,236,257,278,299,320,328,340,360,376,388,398,408,418,427,437,445,447,454,461,468,475,506,567,573,580
])
export.set_date_col0([17,29,20,30,31,32,33,34,35,36,37,38,39,48])
export.set_num_col0([15,18,22,24,25,26,27,28])
export.set_text_col0([])
export.export()
