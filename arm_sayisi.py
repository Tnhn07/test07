#Girilen sayının armstrong sayısı olup olmadığını bulan programı yapınız.

sy1 = int(input('Bir sayı giriniz:'))
str_sy1 = str(sy1)
uzunluk = len(str_sy1)
tpl = 0

for i in range(0,uzunluk):
    x = int(str_sy1[i]) ** uzunluk
    tpl = tpl + x
if tpl == sy1:
    print(tpl,"Bir Armstrong Sayısır.")
else:
    print(sy1,"Bir Armstrong Sayısı değil'dir.")
