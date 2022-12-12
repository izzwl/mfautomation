import argparse
import datetime
import subprocess,sys
import os
sys.path.insert(0,'..')
import X3270


files = [
    "LDB0103A-200101_200331",
    "LDB0103A-200401_200630",
    "LDB0103A-200701_200930",
    "LDB0103A-201001_201231",
    "LDB0103A-210101_210331",
    "LDB0103A-210401_210630",
    "LDB0103A-210701_210930",
    "LDB0103A-211001_211231",
    "LDB0103A-220101_220331",
    "LDB0103A-220401_220630",
    "LDB0103A-220701_220930",
    "LDB0103A-221001_221231",
]

OUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')

nf = open(os.path.join(OUTLIST_DIR,'LDB0103A-JOINED'), "w+") 
nf.write("\n\n\n\n\n\n\n")
for fl in files:
    f = open(os.path.join(OUTLIST_DIR,fl), "r")
    s = 0
    lines = f.readlines()
    for i,l in enumerate(lines):
        if fl == files[0]:
            if l[1:7]=='160050':
                nf.write(l)
        else:
            if l[82:83] in ['1','2','3'] and l[1:7]=='160050':
                nf.write(l)
    f.close()
        