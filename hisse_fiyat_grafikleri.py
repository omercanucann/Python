import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf

hisse = yf.Ticker("ASELS.IS")
data = hisse.history(period="1y")
print(data.head())

# Line Graphics

plt.figure(figsize=(12,6))
plt.plot(data.index, data["Close"], label="Kapanış Fiyatı")
plt.title("Aselsan Hisse Fiyatı (Son 1 Yıl)")
plt.xlabel("Tarih")
plt.ylabel("Fiyat (TRY)")
plt.legend()
plt.show()

#Candle Graphics

mpf.plot(
    data,
    type="candle",        
    style="yahoo",        
    title="ASELS Mum Grafiği (Son 6 Ay)",
    ylabel="Fiyat (TRY)",
    volume=True,         
    mav=(20,50),         
    figratio=(16,9),
    figscale=1.2
)
