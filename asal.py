#Kullanıcın girdiği sayının asal olup olmadığını bulan python programı.
sy1 = int(input("Bir sayı giriniz:"))
tpl = 0
for i in range(2,sy1):
    if sy1 % i == 0:
        tpl = tpl + i
if tpl == 0:
    print("Asal dır")
if tpl != 0:
    print("Asal'değil.")
