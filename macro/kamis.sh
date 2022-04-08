#/bin/bash
python ivr7050u.py --mf=hrc --user=mpmcs99 --runxls=y && \
python ivr7016sts2.py --mf=hrc --user=mpmcs99 --runxls=y && \
python ivr7016.py --mf=hrc --user=mpmcs99 --runxls=y && \
python ivr4025m.py --mf=hrc --user=mpmcs99 --runxls=y 