from datetime import datetime #datetime sınıfı içe aktarılıyor

bugun = datetime.now()

print("Bugün haftanın {}. günü.".format(bugun.weekday()))  # Haftanın kaçıncı günü.(0 dan başlıyor.)
print("{} Yılındayız.".format(bugun.year))   # Yıl bilgisi.
print("{}. Aydayız.".format(bugun.month))   # Ay bilgisi.
print("Ayın {} günündeyiz.".format(bugun.day))   # Gün bilgisi.
print("Saat - {}".format(bugun.hour))   # Saat bilgisi.
print("Dakika - {}".format(bugun.minute))   # Dakika bilgisi.
print("Saniye - {}".format(bugun.second))   # Saniye bilgisi.
print("Tarih - {} / {} / {}".format(bugun.day,bugun.month,bugun.year))   # Tarih bilgisi.
