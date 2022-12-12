#/bin/bash
python iap1600.py --param="" --mf=hrc --user=mpmcs99 --runxls=y && \
python ivr7002.py --mf=hrc --user=mpmcs99 --runxls=y --isrowbawah=y && \
python ivr7020h.py --mf=hrc --user=mpmcs99 --runxls=y && \
python ivr7050u.py --mf=hrc --user=mpmcs99 --runxls=y && \
python ivr7016sts2.py --mf=hrc --user=mpmcs99 --runxls=y && \
python ivr7016.py --mf=hrc --user=mpmcs99 --runxls=y --isrowbawah=y && \
python ivr4025m.py --mf=hrc --user=mpmcs99 --runxls=y --isrowbawah=y