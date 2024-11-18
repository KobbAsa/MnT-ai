import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

np.random.seed(33)
clients = np.random.rand(300, 3) * 300

data = clients.T

n_clusters = 3
cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
    data, c=n_clusters, m=2, error=0.005, maxiter=500, init=None)

cluster_membership = np.argmax(u, axis=0)
cluster_centers = cntr

print("Кластерні центри:\n", cluster_centers)

plt.figure()
plt.scatter(clients[:, 0], clients[:, 1], c='purple', label='Дані клієнтів')

plt.title('Початкові дані')
plt.xlabel('Кількість місячних покупок')
plt.ylabel('Загальна сума покупок')

plt.show()

plt.figure()
plt.plot(jm)

plt.title('Графік зміни цільової функції')
plt.xlabel('Ітерація')
plt.ylabel('Значення цільової функції')

plt.show()

plt.figure()
for i in range(n_clusters):
    plt.scatter(clients[cluster_membership == i, 0], clients[cluster_membership == i, 1], label=f'Кластер {i + 1}')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='x', s=100, label='Центри кластерів')

plt.title('Кластеризація клієнтів залежно від поведінки')
plt.xlabel('Кількість місячних покупок')
plt.ylabel('Загальна сума покупок')

plt.show()

coefficients = []
cluster_range = range(2, 10)
for i in cluster_range:
    cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(data, c=i, m=2, error=0.005, maxiter=500, init=None)
    coefficients.append(fpc)
    print(f"Кількість кластерів: {i} - коефіцієнт розбиття: {round(fpc, 4)}")

plt.figure()

plt.plot(cluster_range, coefficients, c='blue', marker='o')
plt.title("Коефіцієнт розбиття залежно від кількості кластерів")
plt.xlabel("Кількість кластерів")
plt.ylabel("Коефіцієнт розбиття")

plt.xticks(cluster_range)

plt.grid()
plt.show()