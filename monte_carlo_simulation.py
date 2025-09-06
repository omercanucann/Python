import numpy as np
import matplotlib.pyplot as plt

mean_returns = np.array([0.12, 0.08, 0.15])
std_devs = np.array([0.2, 0.1, 0.25])

correlation_matrix = np.array([
    [1.0, 0.2, 0.4],
    [0.2, 1.0, 0.1],
    [0.4, 0.1, 1.0]
])

cov_matrix = np.outer(std_devs, std_devs) * correlation_matrix

num_portfolios = 1000
results = np.zeros((3, num_portfolios))

for i in range(num_portfolios):
    weights = np.random.random(3)
    weights /= np.sum(weights)

    portfolio_return = np.dot(weights, mean_returns)
    portfolio_std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    results[0,i] = portfolio_return
    results[1,i] = portfolio_std
    results[2,i] = portfolio_return / portfolio_std

plt.figure(figsize=(10,6))
plt.hist(results[1,:], bins=50, color='skyblue', edgecolor='black')
plt.title("Monte Carlo Simulasyonu ile Portföy Risk Dağılımı")
plt.xlabel("Portföy Riski (Standart Sapma)")
plt.ylabel("Portföy Sayısı")
plt.show()

plt.figure(figsize=(10,6))
plt.scatter(results[1,:], results[0,:], c=results[2,:], cmap='viridis', marker='o')
plt.xlabel("Portföy Riski (Std Dev)")
plt.ylabel("Portföy Getirisi")
plt.colorbar(label="Sharpe Oranı")
plt.title("Monte Carlo Simulasyonu ile Portföy Dağılımı")
plt.show()