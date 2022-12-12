import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'VRP1300'
filename = args.output if args.output else 'VRP1300.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'CUST','OLD','IPTN','D/F','CUSTOMER-NAME','CONTACT-NAME','CONTACT-PHONE','CONTACT-FAX','EMAIL','ALAMAT1','ALAMAT2','ALAMAT3','ALAMAT4','ALAMAT5','ALAMAT6','ALAMAT7','CREATED','CHANGED','NIK','CS','CUST-CLASS','PT-DI','SBU',
])
export.set_firstlinedata(0)
export.set_popotongan([
    1,5,11,16,20,51,77,96,115,146,177,208,239,270,301,332,352,361,370,379,382,395,401,405,
])
export.set_date_col0([16,17])
export.set_num_col0([])
export.set_text_col0([])
export.export()
