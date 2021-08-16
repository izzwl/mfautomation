import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'SALDOUSD'
filename = args.output if args.output else 'SALDOUSD.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','PGM','NO.WIP','SERIAL#','CUST','START','E.C.D','CUR','NILAI-PENJUALAN-USD','ANGGARAN-MAT-USD','ANGGARAN-M/H-USD','ANGGARAN-OTHER-USD','ANGGARAN-TOTAL-USD','PROFIT-MARGIN(%)','REALISASI-MAT-USD','REALISASI-M/H-USD','REALISASI-OTHER-USD','REALISASI-TOTAL-USD','AKUMULASI-MAT-USD','%','AKUMULASI-M/H-USD','%','AKUMULASI-OTHER-USD','%','AKUMULASI-TOTAL-USD','%','PROSES','AKUM','S','CREATD','NAMA','DESCRIPTION','SBU','CUR=VP40(Y/N)','KURS-USD','TOTAL-QUOTATION','MOS#','CREATED','PENYESUAIAN','P','X','KD-PT-DI'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,5,9,16,37,42,51,60,63,84,105,126,147,168,185,207,228,249,270,291,301,320,330,349,360,379,390,397,402,405,412,443,464,469,471,491,509,521,528,545,549,551,570
])
export.set_date_col0([5,6])
export.set_num_col0([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,34,35,38])
export.export()
