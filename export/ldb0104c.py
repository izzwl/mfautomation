import argparse
import os,sys,re
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
parser.add_argument('--periode', help='210101 210131')
args = parser.parse_args()

periode = args.periode if args.periode else ''
outlist = args.input if args.input else 'LDB0104C'
filename = args.output if args.output else 'LDB0104C.xls'
export = xlsExport(outlist,filename)
font_style = export.font_header_style


#sheet note
export.ws = export.wb.add_sheet('Note')
export.ws.write_merge(0,0,0,2,'ORG CODE', font_style)
export.ws.write(1,0,'No', font_style)
export.ws.write(1,1,'Kolom', font_style)
export.ws.write(1,2,'Keterangan', font_style)
export.ws.write(2,0,'1', font_style)
export.ws.write(2,1,'Tersedia', font_style)
export.ws.write(2,2,'Jumlah jam kehadiran', font_style)
export.ws.write(3,0,'2', font_style)
export.ws.write(3,1,'Terpakai', font_style)
export.ws.write(3,2,'Jumlah jam DWC yang dipergunakan untuk mengerjakan WIP, termasuk 900025 (perintah langsung) + 900009(pertemuan) + 900013(training di dalam), Diambil dari report LDB0104C', font_style)
export.ws.write(4,0,'3', font_style)
export.ws.write(4,1,'Terpakai-WIP', font_style)
export.ws.write(4,2,'Jumlah jam DWC yang dipergunakan untuk mengerjakan WIP, Diambil dari report LDB0104C', font_style)
export.auto_width()

#sheet LDB0104c
export.ws = export.wb.add_sheet('LDB0104C')
export.ws.write_merge(0,1,0,0,'ORG CODE', font_style)
export.ws.write_merge(0,1,1,1,'DESCRIPTION', font_style)
export.ws.write_merge(0,0,2,3,'LABOR', font_style)
export.ws.write(1,2,'I', font_style)
export.ws.write(1,3,'D', font_style)
export.ws.write_merge(0,0,4,7,'DAILY-WORK-CARD', font_style)
export.ws.write(1,4,'HARI-KERJA', font_style)
export.ws.write(1,5,'LEMBUR', font_style)
export.ws.write(1,6,'HARUS', font_style)
export.ws.write(1,7,'SALAH', font_style)
export.ws.write(0,8,'JAM', font_style)
export.ws.write(0,9,'JAM', font_style)
export.ws.write(1,8,'KEHADIRAN', font_style)
export.ws.write(1,9,'JAM LEMBUR', font_style)
export.ws.write_merge(0,0,10,12,'CAJ-HOURS', font_style)
export.ws.write(1,10,'REGULAR', font_style)
export.ws.write(1,11,'OVER-TIME', font_style)
export.ws.write(1,12,'TOTAL', font_style)
export.ws.write_merge(0,0,13,15,'900025-PERINTAH-LANGSUNG', font_style)
export.ws.write(1,13,'REGULAR', font_style)
export.ws.write(1,14,'OVER-TIME', font_style)
export.ws.write(1,15,'TOTAL', font_style)
export.ws.write_merge(0,0,16,18,'900009+900013(RAPAT+TRAINING)', font_style)
export.ws.write(1,16,'REGULAR', font_style)
export.ws.write(1,17,'OVER-TIME', font_style)
export.ws.write(1,18,'TOTAL', font_style)
export.ws.write_merge(0,0,19,21,'WIP-HOURS+900025+900009+900013', font_style)
export.ws.write(1,19,'REGULAR', font_style)
export.ws.write(1,20,'OVER-TIME', font_style)
export.ws.write(1,21,'TOTAL', font_style)
export.ws.write_merge(0,0,22,24,'WIP-HOURS', font_style)
export.ws.write(1,22,'REGULAR', font_style)
export.ws.write(1,23,'OVER-TIME', font_style)
export.ws.write(1,24,'TOTAL', font_style)
# export.get_raw_lines()
# raw_lines = export.raw_lines
# new_raw_lines = []
# for i,l in enumerate(raw_lines):
#     m = re.match(r'[A-Z]{1}[0-9]{4}',l[4:9])
#     if ( m and m.span()[1]==len(l[4:9]) ):
#         new_raw_lines.append(l)
#     if l[17:22] == 'TOTAL':
#         new_raw_lines.append('')
#         new_raw_lines.append(l)
#     if l[0:8].strip() == '0CATATAN':
#         break
# export.raw_lines = new_raw_lines
export.first_line_regex ="^                                                                                                                             "
export.end_line_regex ="^0CATATAN : "
export.set_popotongan([3,10,25,29,34,41,47,54,59,70,81,92,101,112,123,132,143,154,163,174,185,194,205,215,224,235])
export.set_num_col0([int(i) for i in range(8,25)])
export.set_int_col0([int(i) for i in range(2,8)])
export.get_raw_lines()
export.write_body(row=2)
export.auto_width()


#sheet per org
org = {
    'A.sbu_aero_engine' : ['A1100','A1110','A1120','U3110','U3120','U3130','U3140','U3150','U3160','U3410','U3420','U3430','U3440','U3800','U3810',],
    'B.sbu_industrial_turbin' : ['A6410','A6710','A6430'],
}
export.ws = export.wb.add_sheet('PER ORG')
export.ws.write_merge(0,0,0,4,'PT NUSANTARA TURBIN DAN PROPULSI', export.font_bold_style)
export.ws.write_merge(1,1,0,4,'UTILISASI MAN HOUR', export.font_bold_style)
export.ws.write_merge(3,5,0,0,'NO', font_style)
export.ws.write_merge(3,5,1,1,'SBU', font_style)
export.ws.write_merge(3,5,2,2,'ORG', font_style)
export.ws.write_merge(3,3,3,8,'%s'%periode, font_style)
export.ws.write_merge(4,4,3,4,'TERSEDIA', font_style)
export.ws.write_merge(4,4,5,6,'TERPAKAI', font_style)
export.ws.write_merge(4,4,7,8,'TERPAKAI-WIP', font_style)
export.ws.write(5,3,'HR-KERJA', font_style)
export.ws.write(5,4,'LEMBUR', font_style)
export.ws.write(5,5,'MH', font_style)
export.ws.write(5,6,'%', font_style)
export.ws.write(5,7,'MH', font_style)
export.ws.write(5,8,'%', font_style)

row = 6
# print(export.data)
grand_total = {
    'hr_kerja':0,
    'lembur':0,
    'terpakai':0,
    'terpakai_wip':0,
}
baris_sbu = 1
for k,v in org.items():
    if baris_sbu > 1:
        row += 1
    baris_sbu += 1
    judul_sbu = k.replace('_',' ').upper()
    export.ws.write_merge(row,row,1,2,judul_sbu,export.font_bold_style)
    row += 1
    total_per_sbu = {
        'hr_kerja':0,
        'lembur':0,
        'terpakai':0,
        'terpakai_wip':0,
    }
    no = 1
    for i,org_code in enumerate(v):
        for d in export.data:
            if d[0] == org_code:
                export.ws.write(row,0,str(no))
                export.ws.write(row,1,d[0])
                export.ws.write(row,2,d[1])
                export.ws.write(row,3,d[8],export.num_style)
                export.ws.write(row,4,d[9],export.num_style)
                total_tersedia = d[8]+d[9]
                export.ws.write(row,5,d[21],export.num_style)
                persen_terpakai = (d[21]/total_tersedia) if d[21] else 0
                export.ws.write(row,6,persen_terpakai,export.percentage_style)
                export.ws.write(row,7,d[24],export.num_style)
                persen_terpakai_wip = (d[24]/total_tersedia) if d[24] else 0
                export.ws.write(row,8,persen_terpakai_wip,export.percentage_style)
                total_per_sbu['hr_kerja'] += d[8]
                total_per_sbu['lembur'] += d[9]
                total_per_sbu['terpakai'] += d[21]
                total_per_sbu['terpakai_wip'] += d[24]
                no += 1
                row += 1
                break

    export.ws.write(row,2,'Sub Total',export.font_bold_style)
    export.ws.write(row,3,total_per_sbu['hr_kerja'],export.num_bold_style)
    export.ws.write(row,4,total_per_sbu['lembur'],export.num_bold_style)
    total_tersedia = total_per_sbu['hr_kerja']+total_per_sbu['lembur']
    export.ws.write(row,5,total_per_sbu['terpakai'],export.num_bold_style)
    persen_terpakai = (total_per_sbu['terpakai']/total_tersedia)
    export.ws.write(row,6,persen_terpakai,export.percentage_bold_style)
    export.ws.write(row,7,total_per_sbu['terpakai_wip'],export.num_bold_style)
    persen_terpakai_wip = (total_per_sbu['terpakai_wip']/total_tersedia)
    export.ws.write(row,8,persen_terpakai_wip,export.percentage_bold_style)
    grand_total['hr_kerja'] += total_per_sbu['hr_kerja']
    grand_total['lembur'] += total_per_sbu['lembur']
    grand_total['terpakai'] += total_per_sbu['terpakai']
    grand_total['terpakai_wip'] += total_per_sbu['terpakai_wip']
    row +=1
export.ws.write(row,2,'T O T A L',export.font_bold_style)
export.ws.write(row,3,grand_total['hr_kerja'],export.num_bold_style)
export.ws.write(row,4,grand_total['lembur'],export.num_bold_style)
total_tersedia = grand_total['hr_kerja']+grand_total['lembur']
export.ws.write(row,5,grand_total['terpakai'],export.num_bold_style)
persen_terpakai = (grand_total['terpakai']/total_tersedia) if grand_total['terpakai'] else 0
export.ws.write(row,6,persen_terpakai,export.percentage_bold_style)
export.ws.write(row,7,grand_total['terpakai_wip'],export.num_bold_style)
persen_terpakai_wip = (grand_total['terpakai_wip']/total_tersedia) if grand_total['terpakai_wip'] else 0
export.ws.write(row,8,persen_terpakai_wip,export.percentage_bold_style)
export.wb.active_sheet = 2
export.ws.col(0).width = 256 * ( 1 + 5 )
export.ws.col(1).width = 256 * ( 4 + 5 )
export.ws.col(2).width = 256 * ( 20 + 5 )
export.ws.col(3).width = 256 * ( 5 + 5 )
export.ws.col(4).width = 256 * ( 5 + 5 )
export.ws.col(5).width = 256 * ( 5 + 5 )
export.ws.col(6).width = 256 * ( 3 + 5 )
export.ws.col(7).width = 256 * ( 5 + 5 )
export.ws.col(8).width = 256 * ( 3 + 5 )
export.ws.set_panes_frozen(True)
export.ws.set_horz_split_pos(6) 
export.ws.set_vert_split_pos(3) 
export.save_export()

exit()



# #Sheet MT
# export.first_line_regex = "^ WOM    TMWO   BND#"
# export.end_line_regex = "^ WOM    TMWO   TGL"
# export.set_header([
#     'WOM','TMWO','BND#','ISSUED','PART-NUMBER','QTY','RTURN','AVG-PRICE','AVG-PRICE-USD'
# ])
# export.set_firstlinedata(0)
# export.set_popotongan([
#     1,8,15,25,32,53,59,65,79,92,
# ])
# export.set_date_col0([3])
# export.set_num_col0([5,6,7,8])
# export.set_text_col0([])
# export.export_ws('MT')
# export.save_export()

# #Sheet MH
# export.first_line_regex = "^ WOM    TMWO   TGL"
# export.end_line_regex = "^ TMWO#     WOM#       S TOP    JML-MH"
# export.set_header([
#     'WOM','TMWO','TGL','NIK','MENIT','MESIN','RATE-USD','HPK',
# ])
# export.set_firstlinedata(0)
# export.set_popotongan([
#     1,8,15,22,29,33,38,48,52,
# ])
# export.set_date_col0([2])
# export.set_num_col0([4,6,7])
# export.set_text_col0([])
# export.export_ws('MH')
# export.save_export()

# #Sheet MHT
# export.first_line_regex = "^ TMWO#     WOM#       S TOP    JML-MH"
# export.end_line_regex = "^ WIP-WOM X    JML-MH         MAT-IN-RPH"
# export.set_header([
#     'TMWO#','WOM#','S','TOP','JML-MH','MAT-IN-RPH','M/H-IN-RPH','TOT-IN-RPH','MAT-AVG-USD','M/H-IN-USD','TOT-IN-USD','','MAT-IN-USD','MESIN-IN-USD'
# ])
# export.set_firstlinedata(0)
# export.set_popotongan([
#     1,11,17,24,27,37,56,75,94,113,126,141,142,157,174
# ])
# export.set_date_col0([])
# export.set_num_col0([4,5,6,7,8,9,10,12,13])
# export.set_text_col0([])
# export.export_ws('MHT')
# export.save_export()

# #Sheet HPP
# export.first_line_regex = "^ WIP-WOM X    JML-MH         MAT-IN-RPH"
# export.end_line_regex = "^ WOM    P TMWO   STS  REST"
# export.set_header([
#     'WIP-WOM','X','JML-MH','MAT-IN-RPH','MH-IN-RPH','MAT-AVG-USD','MH-IN-USD','PG','CUS','P','S','RST','SERIAL#','PENYESUAIAN-USD','MAT-IN-USD','OPENED','MESIN-USD'
# ])
# export.set_firstlinedata(0)
# export.set_popotongan([
#     1,8,11,20,39,58,77,90,94,98,100,102,106,126,143,158,166,181,
# ])
# export.set_date_col0([15])
# export.set_num_col0([2,3,4,5,6,11,13,14,16])
# export.set_text_col0([])
# export.export_ws('HPP')
# export.save_export()