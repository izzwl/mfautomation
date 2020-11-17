import argparse
import os
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR7030E'
filename = args.output if args.output else 'IVR7030E.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'PR#','DATE','S','WOM#','PG','PART#','DESCRIPTION','STS-3','F','PO#',
    'DATE','S','ITEM','MTU','UNIT-PRICE(PO)','EXT-PRICE(PO)','VENDOR',
    'VENDOR-NAME','NEEDED','PR-QTY','PROMISED','DAYS-LATE','PO-QTY',
    'ACC-QTY','BALANCE','NEW-STOCK','OHC-STOCK','ALT-NEW-STOCK',
    'ALT-OHC-STOCK','SANDI','EXP-CD','UNIT-PRICE(PR)','EXT-PRICE(PR)',
    'MTU','SERIAL#','EXT-PRICE-REQ(RPH)','STATUS-TERAKHIR','SBU',
    'GPR#','F','BYR-M','BYR-P','OWN','MTCD','COND','ACCEPTED',
    'STS-DATE','RFQ#','DATE','BYR','CREATE','PRINT','FINANCE',
    'APPROVE','RFQ','OA','PO','REQ#/ORG','AUTH/NEW-BND','CUST','C',
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,11,19,21,28,31,52,88,95,97,106,114,116,121,124,140,156,164,195,
    202,212,221,231,243,254,265,276,287,302,317,324,330,348,365,370,
    390,409,491,495,500,502,508,514,518,523,528,537,546,555,563,567,
    577,587,597,607,617,627,637,647,660,665
])
export.set_date_col0([1,7,10,18,20,45,46,48,50,51,52,53,54,55,56,58])
export.set_num_col0([14,15,19,22,23,24,25,26,27,28,31,32,35,])
export.export()
