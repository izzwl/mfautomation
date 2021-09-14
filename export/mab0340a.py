import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'MAB0340A'
filename = args.output if args.output else 'MAB0340A.xls'

export = xlsExport(outlist,filename)

#Sheet MT
export.first_line_regex = "^ WOM    TMWO   BND#"
export.end_line_regex = "^ WOM    TMWO   TGL"
export.set_header([
    'WOM','TMWO','BND#','ISSUED','PART-NUMBER','QTY','RTURN','AVG-PRICE','AVG-PRICE-USD'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,8,15,25,32,53,59,65,79,92,
])
export.set_date_col0([3])
export.set_num_col0([5,6,7,8])
export.set_text_col0([])
export.export_ws('MT')
export.save_export()

#Sheet MH
export.first_line_regex = "^ WOM    TMWO   TGL"
export.end_line_regex = "^ TMWO#     WOM#       S TOP    JML-MH"
export.set_header([
    'WOM','TMWO','TGL','NIK','MENIT','MESIN','RATE-USD','HPK',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,8,15,22,29,33,38,48,52,
])
export.set_date_col0([2])
export.set_num_col0([4,6,7])
export.set_text_col0([])
export.export_ws('MH')
export.save_export()

#Sheet MHT
export.first_line_regex = "^ TMWO#     WOM#       S TOP    JML-MH"
export.end_line_regex = "^ WIP-WOM X    JML-MH         MAT-IN-RPH"
export.set_header([
    'TMWO#','WOM#','S','TOP','JML-MH','MAT-IN-RPH','M/H-IN-RPH','TOT-IN-RPH','MAT-AVG-USD','M/H-IN-USD','TOT-IN-USD','','MAT-IN-USD','MESIN-IN-USD'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,11,17,24,27,37,56,75,94,113,126,141,142,157,174
])
export.set_date_col0([])
export.set_num_col0([4,5,6,7,8,9,10,12,13])
export.set_text_col0([])
export.export_ws('MHT')
export.save_export()

#Sheet HPP
export.first_line_regex = "^ WIP-WOM X    JML-MH         MAT-IN-RPH"
export.end_line_regex = "^ WOM    P TMWO   STS  REST"
export.set_header([
    'WIP-WOM','X','JML-MH','MAT-IN-RPH','MH-IN-RPH','MAT-AVG-USD','MH-IN-USD','PG','CUS','P','S','RST','SERIAL#','PENYESUAIAN-USD','MAT-IN-USD','OPENED','MESIN-USD'
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,8,11,20,39,58,77,90,94,98,100,102,106,126,143,158,166,181,
])
export.set_date_col0([15])
export.set_num_col0([2,3,4,5,6,11,13,14,16])
export.set_text_col0([])
export.export_ws('HPP')
export.save_export()