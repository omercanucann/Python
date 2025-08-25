import numpy as np

def tahvil_fiyatlandirma(nominal_deger, kupon_orani, vade, odeme, iskonto):
    kupon_orani = kupon_orani / 100
    iskonto = iskonto / 100
    toplam_donem = vade * odeme
    donemlik_kupon = (nominal_deger * kupon_orani) / odeme
    donemlik_iskonto = iskonto / odeme
    donemler = np.arange(1, toplam_donem + 1)
    kupon_bugunku_deger = donemlik_kupon / (1 + donemlik_iskonto)**donemler
    nominal_bugunku_deger = nominal_deger / (1 + donemlik_iskonto)**toplam_donem
    tahvil_fiyati = np.sum(kupon_bugunku_deger) + nominal_bugunku_deger
    return tahvil_fiyati

while True:
    try:
        nd = float(input("Nominal Değeri Giriniz: "))
        ko = float((input("Kupon Oranını Giriniz(%): ")))
        v = float(input("Vade Giriniz: "))
        odeme_s = int(input("Ödeme Sıklığını Giriniz (Yılda Kaç Defa Ödeme Yapılacak): "))
        isk = float(input("İskonto giriniz(%): "))
        if (nd <= 0 or ko <= 0 or v <= 0 or odeme_s <= 0 or isk < 0):
            print("UYARI: Negatif Değer Girilemez! Lütfen Tekrar Deneyiniz")
        else:
            break
    except ValueError:
        print("Hatalı Değer Girdiniz!")
    
result = tahvil_fiyatlandirma(nd, ko, v, odeme_s, isk)
print(f"Vade Sonundaki Tahvil Fiyatı: {result:.2f}")