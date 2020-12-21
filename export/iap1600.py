import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IAP1600'
filename = args.output if args.output else 'IAP1600.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'SPJ#','L-R#','CREATED','PRINTED','CREATED-BY','S','J','BEBAN',
    'PG','WOM#','STATUS','S','DATE-7','CUST','SANDI','ONWING',
    'ANTAR-ENG','HR-LBR','UM-AKOM','REFERENSI','KEPERLUAN','NIK','NAMA',
    'ORG','D','GRADE','GOL','JOB-TITLE','S','K',
    'R#','NO','KD','KOTA/NEGARA','BERANGKAT','PULANG','HR','TRNSPT',
    'BBM','VOUCHER#','TANGGAL','NILAI-VOUCHER-RPH','CC','LAP','KH',
    'MTU','U-BENSIN/TOL','U-TRP-PP','U-TAMBAHAN','U-AKOM-LUMPSUM',
    'U-TRP-LOKAL','U-MAKAN','U-SAKU','U-ONWING','ALLOWANCE-LN',
    'NIL-SUSULAN','NILAI-VOUCHER','UM/BYR','NILAI-PJK','NO-BM',
    'TGL-BM',
])
export.set_firstlinedata(1)
export.set_popotongan([
    1,11,16,24,32,42,45,47,54,57,64,80,82,90,95,101,108,118,125,
    133,164,215,222,248,254,256,262,266,282,284,286,289,292,295,316,
    326,336,339,346,350,360,367,387,393,397,400,404,417,432,447,462,
    477,492,507,522,537,552,569,577,593,603,611
])
export.set_date_col0([2,3,12,34,35,40])
export.set_num_col0([41,46,47,48,49,50,51,52,53,54,55,56,58])
export.export()
