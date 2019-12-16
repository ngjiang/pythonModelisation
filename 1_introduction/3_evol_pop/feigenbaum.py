# Diagramme de Feigenbaum
K = 1
Nbpoint = 250

import matplotlib.pyplot as plt
debut = int(2.8 * Nbpoint)
fin = int(4. * Nbpoint)+1
for r in range(debut, fin, 1):
	print('r =', r/Nbpoint)
	N0 = .01
	for t in range(200):
		N0 = r / Nbpoint * N0 * (1 - N0/K)
		if t > 100 :
			plt.plot(r / Nbpoint, N0, 'k.', markersize=1)

plt.xlabel('Taux de croissance : r', fontsize='medium')
plt.ylabel('Population limite', fontsize='medium')
plt.show()

