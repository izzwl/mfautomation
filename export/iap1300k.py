import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'IAP1300K'
filename = args.output if args.output else 'IAP1300K.xls'

export = xlsExport(outlist,filename)
export.set_header(['KODE','NO-PEMB.','CREATED','NIK','P','PG','SANDI','NOMOR-SURAT/REF','TGL-REF','VOUCHER#','MTU','NILAI','NILAI-PPN','VEND/NIK','DESC/NAMA','URAIAN','NILAI-VOUCHER-RPH','SBU','PO#','NILAI-PPH','NILAI-DENDA','NILAI-LAIN','NILAI-INVOICE','JNS','COST','REF-VCHR','REF-NP'])
export.set_firstlinedata(0)
export.set_popotongan([
    1,7,16,24,31,33,36,42,63,71,81,84,105,123,133,164,214,237,242,252,270,288,306,324,328,335,345,356,
])
export.set_date_col0([2,8,])
export.set_num_col0([11,12,16,19,20,21,22])
export.export()
