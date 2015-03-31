###################Liwen Tian
##################Assignment6
##############this module computes the Mandelbrot fractal using the Mandelbrot iteration##
#######################################################################################

import numpy as np
import matplotlib.pyplot as plt
import warnings

def mandelbrot(h,w,N_max = 50):
	'''returns an image of the Mandelbrot fractal of size(h,w)'''
	warnings.warn("nomatter",RuntimeWarning)
	x,y=np.ogrid[-2:1:500j,-1.5:1.5:500j]
	c = x + 1j*y
	z = c
	iterationNum = []
	some_threshold = 50
	try:
		for v in range(N_max):
			num  =  v
			# iterationNum.append(print_number)
			z = z**2 + c
			mask = np.abs(z) < some_threshold
	except RuntimeWarning:
		print ("Warning")

	plt.imshow(mask.T,extent = [-2,1,-1.5,1.5])
	plt.gray()
	plt.savefig('mandebrot.png')
	
	return 	None
######################################################################################
#############################this part is not to present the warning when running the program######	
with warnings.catch_warnings():
	warnings.simplefilter("ignore")
	mandelbrot(50,50)