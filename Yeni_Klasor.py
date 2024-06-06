import random
import time

print("Selam, Uygulamaya hoş geldiniz!")
time.sleep(3)

tekrar = int(input("Kaç adet şifre istersiniz?"))
                   
for i in range(tekrar):
    karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    

    uzunluk = int(input("Parola uzunluğunu girin: "))
    isim = (input("Bir kullanıcı ismi girin, Sayısal değer içermemeli!"))

    parola = ""
    
        
    for i in range(uzunluk):
        parola += random.choice(karakterler)
    

    parola += isim

    print(f" {isim} için oluşturulan Parola:  {parola}")


