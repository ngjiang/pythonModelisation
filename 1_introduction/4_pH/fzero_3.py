from pylab import *
def fzero(C, K, h):
	
	C = array(C).T
	K = array(K).T

	Ke = 1e-14
	
	Nligne = size(C, axis=0)
	Ncolonne = size(C, axis=1)
	C0 = dot(ones((Nligne, 1)), array([sum(C, axis=0)]))
	ConCat = concatenate((ones((1, Ncolonne)), K/h), axis=0)
	alphanum = cumprod(ConCat, axis=0)
	alphadenom = dot(ones((Nligne,1)), array([sum(alphanum, axis=0)]))
	conc = C0 * alphanum / alphadenom
	ksi = sum(cumsum(ones((Nligne, Ncolonne)), axis=0) * (conc-C))
	return ksi + Ke/h - h

