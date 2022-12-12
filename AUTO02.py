import datetime
import BCINBC40,BCOUTBC3

now = datetime.datetime.now()
bcin = 'BELUM'
try:
    bcin = BCINBC40.handle()
except:
    bcin = 'SUBHANALLAH'


if bcin == 'ALHAMDULILLAH':
    try:
        bcout = BCOUTBC3.handle()
    except:
        bcout = 'SUBHANALLAH'
else:
    bcout = 'BELUM, cek BCINBC40'


print("BCINBC40 %s"%bcin)
print("BCOUTBC3 %s"%bcout)
