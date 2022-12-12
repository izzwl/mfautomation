import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'PPB1300H'
filename = args.output if args.output else 'PPB1300H.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'WOM#','SER#','CUST','PPCL#','METTAG','SEQ','PART#-OFF','DESCRIPTION-OFF',
    'SERIAL#-OFF','QTY','TSN','TSO','CSN','CSO','REMOVED','REMARKS','PART#-ON',
    'DESCRIPTION-ON','SERIAL#-ON','QTY','TSN','TSO','CSN','CSO','INSTALLED',
    'REMARKS','ORIG-PO-PRICE','MTU','PO#','COND','OHC-AVG-PRICE',
    'NEW-AVG-PRICE','PRICE-LIST','TH','UNIT-PRICE','TGL-SUB','KD',
    'DESKRIPSI','DISPO','PP08','PP12'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,8,29,34,47,55,59,80,101,126,130,138,146,152,158,179,200,221,242,267,271,
    279,287,293,299,320,340,359,363,372,376,394,412,425,428,446,454,458,483,
    489,495,499,
])
export.set_date_col0([33])
export.set_num_col0([9,19,26,30,31,32,34])
export.set_text_col0([])
export.export()
