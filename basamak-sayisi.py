import time
programtanitimi = "Bu program, girmek olduğunuz sayının basamak uzunluğunu bulur."
print("."*len(programtanitimi), programtanitimi, "."*len(programtanitimi), sep="\n", end="\n\n")


try:
    isteksayi = input("Basamak sayısını öğrenmek istediğiniz sayıyı giriniz: ")
    sayi = str(isteksayi)
    print(f"Girmiş olduğunuz sayının basamak uzunluğu: {len(sayi)}")       

except ZeroDivisionError:
    print("Yanlış bir işlem yaptınız. Lütfen sayı girdiğinizden emin olunuz!")

finally:
    sayac = 10
    while sayac > 0:
        print("\rSistemden çıkılıyor.. Son {} saniye...".format(sayac), end="")
        time.sleep(1)
        sayac -= 1
    


