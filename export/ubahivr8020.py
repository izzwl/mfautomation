
import sys
import os

MFOUTLIST_DIR = os.path.join(os.path.expanduser("~"),'mfoutlist')
SRC = 'IVR8020'
DST = 'IVR8020-NEW'
print(sys.getrecursionlimit())
sys.setrecursionlimit(30000)

nf = open(os.path.join(MFOUTLIST_DIR,DST), "w+") 
f = open(os.path.join(MFOUTLIST_DIR,SRC), "r")

lines = f.readlines()
s = 0
def write_lines(s,matclass,lines):
    i = s
    if lines[i][1:8] == 'IVR8020':
        matclass = lines[i+2][1:22]
    
    l = matclass.rjust(21,' ') + lines[i]
    nf.write(l)
    s += 1    
    if len(lines) > (s):
        return write_lines(s,matclass,lines)

write_lines(s,'',lines)