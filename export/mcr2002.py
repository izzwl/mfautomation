import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'MCR2002-DETAIL'
filename = args.output if args.output else 'MCR2002-DETAIL.xls'

export = xlsExport(outlist,filename)

#Sheet RESUME
export.first_line_regex = "^ K-ORG  NIK    NAMA                           REKENING            JUMLAH"
export.end_line_regex = "^ K-ORG  NIK    NAMA                           REALISASI"
export.end_line_regex_offset = -3
export.set_header([
    'K-ORG','NIK','NAMA','REKENING','JUMLAH',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,8,15,46,62,73,
])
export.set_date_col0([])
export.set_num_col0([4])
export.export_ws('RESUME')
export.save_export()

#Sheet DETAIL
export.first_line_regex = "^ K-ORG  NIK    NAMA                           REALISASI"
export.end_line_regex = None
export.end_line_regex_offset = 0

export.set_header([
    'K-ORG','NIK','NAMA','REALISASI','SEQ','BLN','KD','PENYAKIT','TGL','DOKTER','OBAT','JML','K'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,8,15,44,56,59,63,66,87,94,102,110,117,119,
])
export.set_date_col0([8])
export.set_num_col0([3,9,10,11])
export.export_ws('DETAIL')
export.save_export()

