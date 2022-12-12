import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IAP1300B'
filename = args.output if args.output else 'IAP1300B.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'KODE','NO-PEMB.','CREATED','NIK','P','PG',
    'SANDI','NOMOR-SURAT','TANGGAL','NO-CEK-LC','NAMA-BANK','NO-REKENING','VOUCHER#','MTU','NILAI','NILAI-PPN','VEND/NIK','DESC/NAMA','URAIAN','NILAI-VOUCHER-RPH','SBU','PO#','NILAI-PPH','NILAI-DENDA','NILAI-LAIN','NILAI-INVOICE','JNS','COST','REF-VCHR','REF-NP'
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,7,16,24,31,33,36,42,58,66,82,96,117,127,131,154,170,180,211,267,285,290,298,317,335,353,371,375,381,392,401,
])
export.set_date_col0([2,8,])
export.set_num_col0([14,15,19,22,23,24,25])
export.export()
