#/bin/bash
python ivr1325.py \
    --param"2209010000000 2209309999999 0" \
    --user=mpmcs99 --mf=hrc --runxls=y &&\
python ivr1326.py \
    --param"2209010000000 2209309999999" \
    --user=mpmcs99 --mf=hrc --runxls=y &&\
python ivr1321b.py \
    --param"2209010000000 2209309999999 0" \
    --user=mpmcs99 --mf=hrc --runxls=y &&\
python ivr1320b.py \
    --param"2209010000000 2209309999999" \
    --user=mpmcs99 --mf=hrc --runxls=y &&\
python ivr7016all.py \
    --param="R2200001 R2299999 X" \
    --user=mpmcs99 --mf=hrc --runxls=y &&\
exit