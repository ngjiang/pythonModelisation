# Les différents types d'évolution

K = 1

def croissance(N0, T, r):
	
	N = []
	N.append(N0)
	for t in range(T):
		N0 = r * N0 * (1 - N0/K)
		N.append(N0)

	tps = range(0, T+1, 1)
	return tps, N

import matplotlib.pyplot as plt
tps, N = croissance(0.05, 50, 2.5)
plt.plot(tps, N, 'k-')
tps, N = croissance(0.05, 50, 2)
plt.plot(tps, N, 'k-')
tps, N = croissance(0.05, 50, 1.5)
plt.plot(tps, N, 'k-')
plt.xlabel("Temps", fontsize='medium')
plt.ylabel("cellules tumorales", fontsize='medium')
plt.show()

tps, N = croissance(0.05, 50, 3)
plt.plot(tps, N, 'k-')
plt.xlabel("Temps", fontsize='medium')
plt.ylabel("cellules tumorales", fontsize='medium')
plt.show()

tps, N = croissance(0.05, 50, 3.5)
plt.plot(tps, N, 'k-')
plt.xlabel("Temps", fontsize='medium')
plt.ylabel("cellules tumorales", fontsize='medium')
plt.show()

tps, N = croissance(0.01, 90, 3.9)
plt.plot(tps, N, 'k-')
plt.xlabel("Temps", fontsize='medium')
plt.ylabel("cellules tumorales", fontsize='medium')
plt.show()

tps, N = croissance(0.01+10**-10, 90, 3.9)
plt.plot(tps, N, 'k-')
plt.xlabel("Temps", fontsize='medium')
plt.ylabel("cellules tumorales", fontsize='medium')
plt.show()





