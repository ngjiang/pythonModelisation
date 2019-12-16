from fzero_3 import fzero

def calculpH(C, K):
	a = -3.
	b = 18.
	epsi = 1e-2
	# Algorithme de dichotomie
	while(abs(b-a) > epsi):
		c = (a+b)/2.
		if(fzero(C, K, 10**(-c)) * fzero(C, K, 10**(-a)) > 0):
			a = c
		else:
			b = c
	return c

K = [\
[10**-3.1, 10**-4.8, 10**-6.4],\
[10**-1.8, 10**-7.2, 0],\
[10**-9.2, 0, 0,]]
C = [\
[0.1, 0, 0, 0],\
[0.1, 0, 0, 0],\
[0, 0.6, 0, 0]]
print(calculpH(C, K))
