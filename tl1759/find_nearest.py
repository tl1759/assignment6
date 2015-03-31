# ####Liwen Tian
# ###Assignment6_3

# #####this module generates a 10 x 3 array of random numbers in the range[0,1]###########
import numpy as np 

array = np.random.rand(10,3)
b = 0.5
####array and specific value are given by the instsruction########
#########################################################
def find_nearest(array,a0):
	nearestList = []
	"""use abs and argsort to find the colunm for each of the number cloest to a specific value"""
	for row in array:
		idxList = np.abs(row-a0).argsort()
		idxele = row.flat[idxList[0]]
		nearestList.append(idxele)
	return nearestList



