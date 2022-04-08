import argparse
from datetime import date, datetime, time
import os,sys,re

from numpy import iterable
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from xlsExport import xlsExport
MFOUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')

parser = argparse.ArgumentParser()
parser.add_argument('--input_ldb0103a', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--input_ldb0103g', help='input file select - must be on ~/mfoutlist')
parser.add_argument('--output', help='output file name ~/mfxls')
args = parser.parse_args()

outlist_a = args.input_ldb0103a if args.input_ldb0103a else 'LDB0103A'
outlist_g = args.input_ldb0103g if args.input_ldb0103g else 'LDB0103G'
filename = args.output if args.output else 'KEKJK.xls'

export = xlsExport(outlist_a,filename)
export.set_header([
    'NIK','NAMA','GR','ORG','NAMA-ORG','TGL','KD','J-DAT','J-PUL','LDAT','LPUL',
    'LTOT','LIBUR','LBH-T','LBH-L','ATH'
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,8,39,42,48,74,82,85,91,97,102,107,112,118,124,130,132
])
export.set_date_col0([5])
export.set_num_col0([])
export.export_ws('ldb0103a')
data_ldb0103a = export.data

export = xlsExport(outlist_g,filename)
export.set_header([
    'NIK','NAMA','KD-ORG','TANGGAL','OUT','IN','MENIT','IST','SIK','URAIAN-KEPERLUAN-DINAS',
])
export.set_firstlinedata(5)
export.set_popotongan([
    1,9,36,44,53,60,67,75,79,83,120
])
export.set_date_col0([3])
export.set_num_col0([])
export.end_line_regex ="^.*RESUME - ORG$"
export.end_line_regex_offset = -3

export.get_raw_lines()
raw_lines = export.raw_lines
new_raw_lines = []
for i,l in enumerate(raw_lines):
    m = re.match(r'[0-9]{6}',l[1:7])
    if ( m and m.span()[1]==len(l[1:7]) ):
        new_raw_lines.append(l)
export.override_raw_lines = new_raw_lines
export.export_ws('ldb0103g')
data_ldb0103g = export.data

file_kekjk = open(os.path.join(MFOUTLIST_DIR,'KEKJK'), "w+")
file_kekjk.write('')
file_kekjk.close()
file_kekjk = open(os.path.join(MFOUTLIST_DIR,'KEKJK'), "a+")

print('TEST')
data = []
for da in data_ldb0103a:
    da_nik = da[0]
    da_tgl = da[5]
    da_kdhr = da[6]
    da_in = da[7]
    da_out = da[8]
    absen = {
        'nik': da[0],
        'nama': da[1],
        'org': da[3],
        'tgl': da[5],
        'tgl_str': da[5].strftime("%Y-%m-%d"),
        'kdhr': da[6],
        'cek_in': da[7],
        'cek_out': da[8],
        'ath': da[15],
        'gate':[],
        'kek_jam_kerja':0,
        'kek_istirahat':0,
        'kek_total':0
    }
    # print("A:",da[0],da[5].strftime("%Y-%m-%d"),da[6],da[7],da[8])
    # file_kekjk.write("A:"+da[0]+da[5].strftime("%Y-%m-%d")+da[6]+da[7]+da[8])
    for dg in data_ldb0103g:
        if absen['nik'] == dg[0] and absen['tgl'] == dg[3]:
            absen['gate'].append({
                'cek_out': dg[4],
                'cek_in': dg[5],
                'menit': dg[6],
                'ist': dg[7],
                'sik': dg[8],
            })
        # print("G:",dg[0],dg[3].strftime("%Y-%m-%d"),dg[4],dg[5],dg[6],dg[7],dg[8],)
        # file_kekjk.write("G:"+dg[0]+dg[3].strftime("%Y-%m-%d")+dg[4]+dg[5]+dg[6]+dg[7]+dg[8])
    data.append(absen)
jam_masuk = datetime.combine(date.today(),time(7,30))
jam_pulang = datetime.combine(date.today(),time(16,30))
ist_awal = datetime.combine(date.today(),time(7,30))
ist_akhir = datetime.combine(date.today(),time(16,30))
kekjk = []
for absen in data:
    if absen['kdhr'] == "1":
        kek_jam_kerja = 0
        absen_masuk = datetime.combine(date.today(),time(*[int(x) for x in absen['cek_in'].split(".")]))
        absen_pulang = datetime.combine(date.today(),time(*[int(x) for x in absen['cek_out'].split(".")]))
        if absen['cek_in']!='00.00' and (absen_masuk > jam_masuk):
            delta_masuk = absen_masuk - jam_masuk
            if delta_masuk.seconds > 0:
                kek_jam_kerja += int(delta_masuk.seconds/60)
        if absen['cek_out']!='00.00' and (absen_pulang < jam_pulang):
            delta_pulang = jam_pulang - absen_pulang
            if delta_pulang.seconds > 0:
                kek_jam_kerja += int(delta_pulang.seconds/60)
        absen['kek_jam_kerja'] = kek_jam_kerja
        
        kek_istirahat = 0
        for gate in absen['gate']:
            try:
                gate_masuk = datetime.combine(date.today(),time(*[int(x) for x in gate['cek_in'].split(":")])) if gate['cek_in'] != "??" else None
            except:
                gate_masuk = None
            try:    
                gate_keluar = datetime.combine(date.today(),time(*[int(x) for x in gate['cek_out'].split(":")])) if gate['cek_out'] != "??" else None
            except:
                gate_keluar = None
            if gate['menit'] != "" :
                menit = int(gate['menit'])
                if menit > 0 and gate['sik'] ==" P":
                    kek_istirahat += menit
            else:
                if absen['ath'] == 'IG' and not gate_masuk:
                    if gate_keluar < ist_awal:
                        delta = ist_awal - gate_keluar
                        kek_istirahat += int(delta.seconds/60)
                    elif gate_keluar > ist_awal and gate_keluar < ist_akhir:
                        delta = jam_pulang - ist_akhir
                        kek_istirahat += int(delta.seconds/60)
                    elif gate_keluar > ist_akhir:
                        delta = jam_pulang - gate_keluar
                        kek_istirahat += int(delta.seconds/60)
        absen['kek_istirahat'] = kek_istirahat
        absen['kek_total'] = absen['kek_jam_kerja'] + absen['kek_istirahat']
        line_data = absen['org']+' '+absen['nik']+' '+absen['nama']+' '+absen['tgl_str']+' '+str(absen['kek_jam_kerja'])+' '+str(absen['kek_istirahat'])+' '+str(absen['kek_total'])+' '+'\n'
        file_kekjk.write(line_data)
        kekjk.append({
            'org' : absen['org'],
            'nik' : absen['nik'],
            'nama' : absen['nama'],
            'tgl_str' : absen['tgl_str'],
            'kek_jam_kerja' : absen['kek_jam_kerja'],
            'kek_istirahat' : absen['kek_istirahat'],
            'kek_total' : absen['kek_total'],
        })

file_kekjk.close()



file_kekjk_sum = open(os.path.join(MFOUTLIST_DIR,'KEKJK_SUM'), "w+")
file_kekjk_sum.write('')
file_kekjk_sum.close()
file_kekjk_sum = open(os.path.join(MFOUTLIST_DIR,'KEKJK_SUM'), "a+")
kek_jam_kerja = 0
kek_istirahat = 0
kek_total = 0
line_data = {}
for i,k in enumerate(kekjk):
    if i==0:
        nik_lama = k['nik']
    
    if k['nik'] == nik_lama:
        kek_jam_kerja += k['kek_jam_kerja']
        kek_istirahat += k['kek_istirahat']
        kek_total += k['kek_total']
    else:
        kek_jam_kerja = k['kek_jam_kerja']
        kek_istirahat = k['kek_istirahat']
        kek_total = k['kek_total']

    line_data[k['nik']]= [kek_total,
        k['org']+' '+\
        k['nik']+' '+\
        k['nama']+' '+\
        str(kek_jam_kerja)+' '+\
        str(kek_istirahat)+' '+\
        str(kek_total)+' '+'\n'
    ]
    if i>0:
        nik_lama = k['nik']


for k,v in line_data.items():
    if v[0] > 0:
        file_kekjk_sum.write(v[1])    
file_kekjk_sum.close()