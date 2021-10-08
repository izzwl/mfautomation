import argparse
import os,sys,re
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist = args.input if args.input else 'MCR2008'
filename = args.output if args.output else 'MCR2008.xls'

export = xlsExport(outlist,filename)
export.set_header(['NO.','KDORG','DESCRIPTION','NIK','NAMA','JOB-CD','','RUMPUN','JOB-TITLE','STS-JOB','JENIS','TMT','GR','IN','F','J','S','J','H','P','DESCRIPTION','K','A','GL','MK','M','C','LAHIR','TMT-UMC','TMTKGG','TMT-CB','TMT-IPTN','TEMPAT-LAHIR','DARAH','NIK-1','NAMA-1','ORG-1','NIK-2','NAMA-2','ORG-2','TMT-GRD','NOMOR-KTP','NO-PASPOR','EXP-DTE','NO-NPWP','NO-ASTEK'])
export.set_firstlinedata(0)
export.set_pivot_year(1950)
export.set_popotongan([1, 6, 12, 38, 45, 76, 83, 86, 107, 138, 146, 153, 161, 164, 167, 169, 171, 173, 175, 177, 180, 201, 203, 205, 207, 211, 213, 215, 224, 232, 240, 248, 259, 281, 287, 294, 325, 331, 338, 369, 375, 383, 400, 410, 418, 439, 452])
export.set_date_col0([11,27,28,29,30,31,40,43])
export.set_num_col0([])
export.set_text_col0([])
export.first_line_regex ="^0NO.  KDORG DESCRIPTION               NIK"
export.get_raw_lines()
raw_lines = export.raw_lines
new_raw_lines = []
for i,l in enumerate(raw_lines):
    m = re.match(r'[0-9]{6}',l[38:44])
    if ( m and m.span()[1]==len(l[38:44]) ):
        new_raw_lines.append(l)
export.override_raw_lines = new_raw_lines
export.export()