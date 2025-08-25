import numpy as np

hisse_sayisi = int(input("Kaç adet hisse senedi gireceksiniz? "))
gun_sayisi = int(input("Her Hisse için kaç günlük getiri gireceksiniz? "))

getiriler_list = []

for i in range(hisse_sayisi):
    while True:
        veri = input(f"{i+1}. Hisse için {gun_sayisi} günlük getiriyi aralarında boşluk bırakarak giriniz ")
        try:
            getiriler = np.array(list(map(float, veri.strip().split())))
            if len(getiriler) != gun_sayisi:
                print(f"Lüften {gun_sayisi}'nı tam olarak giriniz. ")
                continue
            getiriler_list.append(getiriler)
            break
        except ValueError:
            print("Hatalı giriş!")

getiriler_array = np.array(getiriler_list).T
ortalama_getiri = np.mean(getiriler_array, axis=0)
varyans = np.var(getiriler_array, axis=0)
std_sapma = np.std(getiriler_array, axis=0)
kovaryans = np.cov(getiriler_array.T)

risk_rate = 0.0005
sharpe_ratio = (ortalama_getiri - risk_rate) / std_sapma

agirliklar = np.array([1/hisse_sayisi]*hisse_sayisi)
getiri = np.dot(ortalama_getiri, agirliklar)
portfoy_risk = np.sqrt(np.dot(agirliklar.T, np.dot(kovaryans, agirliklar)))
if portfoy_risk == 0:
    portfoy_sharpe = float('inf')
else:
    portfoy_sharpe = (getiri - risk_rate) / portfoy_risk

print("\n--- Hisse Bazında Analiz ---")
for i in range(hisse_sayisi):
    print(f"{i+1}. Hisse:")
    print(f"  Ortalama Getiri: {ortalama_getiri[i]:.4f}")
    print(f"  Varyans: {varyans[i]:.4f}")
    print(f"  Standart Sapma (Risk): {std_sapma[i]:.4f}")
    print(f"  Sharpe Oranı: {sharpe_ratio[i]:.4f}")
    print("-" * 30)

print("\n--- Portföy Analizi (Eşit Ağırlıklı) ---")
print(f"Portföy Ortalama Getiri: {getiri:.4f}")
print(f"Portföy Toplam Risk (Standart Sapma): {portfoy_risk:.4f}")
print(f"Portföy Sharpe Oranı: {portfoy_sharpe:.4f}")

print("\nKovaryans Matrisi (Hisseler arası ilişki):")
print(np.round(kovaryans, 4))