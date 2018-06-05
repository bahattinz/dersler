from datetime import datetime
from business import *

GUNCEL_FIYAT=80000

a=(SuratTeknesi)Vasita("mmjk","msds",yakit=YakitTuru.BENZIN)
print(a.arac_tipi())

def fiyat_hesapla():
    global GUNCEL_FIYAT
    m=Motosiklet("Kawasaki","Z750",YakitTuru.BENZIN)
    m.yil=2012
    yas = datetime.now().year -m.yil
    print("{}, yas:{}".format(m,yas))
    for y in range(yas):
        if y==0:
            GUNCEL_FIYAT=GUNCEL_FIYAT-5000
        else:
            GUNCEL_FIYAT-=2000

    print("GÜNCEL FİYAT:{}".format(GUNCEL_FIYAT))

# fiyat_hesapla()
