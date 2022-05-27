from datetime import datetime
bugun = datetime.today()
gunler = ["Pazar","Pzt","Salı","çrşm","Prşmb","Cuma","Cmt","PZr"]
gun = int(input("Gün gir:"))
ay = int(input("Ay gir:"))
yil = int(input("Yıl gir:"))
dogum_tarihi = datetime(year = yil , month = ay , day = gun)
print(dogum_tarihi)
dgm = int(dogum_tarihi.strftime('%w'))
print(gunler[dgm])
