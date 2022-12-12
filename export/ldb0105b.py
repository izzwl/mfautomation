import argparse
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'LDB0105'
filename = args.output if args.output else 'LDB0105.xls'

export = xlsExport(outlist,filename)
export.set_header([
    'NO.','NIK','NAMA','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31',
])
export.set_firstlinedata(1)
export.set_popotongan([
    2,6,13,40,43,46,49,52,55,58,61,64,67,70,73,76,79,82,85,88,91,94,97,100,103,106,109,112,115,118,121,124,127,130,133,
])
export.set_date_col0([])
export.set_num_col0([])
export.export()
