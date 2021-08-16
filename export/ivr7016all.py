import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IVR7016'
filename = args.output if args.output else 'IVR7016.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'PR#','CREATED','S','DATE','BY','PG','WOM#','CUST','SERIAL#','PART#',
    'DESCRIPTION','C','STS-3','RFQ#','DATE','PO#','ITEM','DATE','S','C','PT',
    'VENDOR','VENDOR-NAME','MTU','UNIT-PRICE(PO)','EXT-PRICE(PO)','PR-QTY',
    'PO-QTY','PO-EDD','RECVD-DATE','RECVD-QTY','INSP-DATE','STORE-DATE',
    'STORE-QTY','DR-QTY','DR#','BA/BP#','DATE','NP#','TYPE','DATE','VOUCHER#',
    'DATE','PAYMENT#','DATE','STATUS-TERAKHIR','REMARK-ITEM-PO','SHIPPED',
    'RECEIVED','AWB/BL/SJ','SANDI','REV','BY','DATE','REQ#/ORG','CREATED',
    'AUTHORIZED','UNIT-PRICE(PR)','MTU','PRICE-LIST','TH','BYR','S3-BY','GPR#',
    'COND','CONSIG'
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,11,19,21,29,37,40,47,52,73,94,130,132,141,150,158,167,172,180,182,185,
    188,195,226,230,245,261,271,282,294,305,316,327,337,348,360,371,381,389,
    399,404,412,422,430,440,448,529,574,582,591,612,618,623,630,638,648,656,
    667,686,690,703,707,712,719,724,729,735
])
export.set_date_col0([1,3,12,14,17,28,29,31,32,37,40,42,44,47,48,53,55,56])
export.set_num_col0([24,25,26,27,30,33,34,57,59])
export.export()
