import datetime
import BCINBC23,BCOUTBC25,WOMAKTIF,IVR7020H,BCIN72,BCMR02

now = datetime.datetime.now()
bcin = 'BELUM'
try:
    bcin = BCINBC23.handle()
except:
    bcin = 'SUBHANALLAH'

if bcin == 'ALHAMDULILLAH':
    try:
        bcin72 = BCIN72.handle()
    except:
        bcin72 = 'SUBHANALLAH'

if bcin72 == 'ALHAMDULILLAH':
    try:
        bcmr02 = BCMR02.handle()
    except:
        bcmr02 = 'SUBHANALLAH'

if bcmr02 == 'ALHAMDULILLAH':
    try:
        bcout = BCOUTBC25.handle()
    except:
        bcout = 'SUBHANALLAH'
else:
    bcout = 'BELUM, cek BCINBC23'

if bcout == 'ALHAMDULILLAH':
    try:
        wom = WOMAKTIF.handle()
    except:
        wom = 'SUBHANALLAH'
else:
    wom = 'BELUM, cek BCOUTBC25'

if now.strftime('%w') == '1':
    try:
	ivr7020h = IVR7020H.handle()
    except:
	ivr7020h = 'SUBHANALLAH'
else:
    ivr7020h = 'BELUM'

print("BCINBC23 %s"%bcin)
print("BCOUTBC25 %s"%bcout)
print("WOMAKTIF %s"%wom)
print("IVR7020H %s"%ivr7020h)
