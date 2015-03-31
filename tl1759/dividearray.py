### Liwen Tian
### Assignment6_2


##### this is a module that divide a given array's ###########
#########eaah column element - wise with another array ######
import numpy as np 

def dividearray():
	a = np.arange(25).reshape(5,5)
	b = np.array([1.,5,10,15,20])
	c = np.divide(a,b)
	return c  

###################################