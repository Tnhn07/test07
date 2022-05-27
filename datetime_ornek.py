# 1 ocak 1901 den 31 aralık 2000 e kadar kaç sefer bir ayın ilk günü pazar olur?
from datetime import datetime

suan = datetime.now()
pazar_sayisi = 0

for yil in range(1901,2001):
    for ay in range(1,13):
        if datetime(yil,ay,1).isoweekday() == 7: #Eğer 1 ayın ilk günü pazar ise pazar_sayisi değişkenini 1 arttır.
            pazar_sayisi = pazar_sayisi + 1
print(pazar_sayisi)
