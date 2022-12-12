import argparse
import requests
import os,sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')
from settings import API_URL,MFOUTLIST_DIR

parser = argparse.ArgumentParser()
parser.add_argument('--jenis', help='jenis BCIN XX')
parser.add_argument('--input', help='input file select - must be on ~/mfoutlist')
args = parser.parse_args()

jenis = args.jenis
if not jenis:
    exit('jenis harus diisi')
outlist = args.input if args.input else jenis

files = {
    'file_uploaded': open(os.path.join(MFOUTLIST_DIR,outlist), 'rb'),
}
data = {
    'jenis': jenis,
}
r = requests.post(API_URL, data=data, files=files)
print(r.headers)
print(r.status_code)
if r.status_code == 200:
    json = r.json()
    for j in json:
        print(j)
