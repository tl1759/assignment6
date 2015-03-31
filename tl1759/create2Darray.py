###########################################################################
## Liwen Tian
## Assignment 6
#this module creates a 2-D array(without typing explicitly)
#############create 2D array ##################### 
import numpy as np
####################################################################################
############## create a 2-Darray  shown on the introduction with specific start and end########
class create2Darray:
	"""This is a 2D-array class with the given numbers"""
	def generate(self,rangescale,row,col):
		arrayList = []
		global array2d
		array2d = (np.arange(rangescale).reshape(col,row)+1).transpose()
		return array2d

####################################################################################

##########Generate a new array containing specifix rows###############
	def extract_rows(slef,start,end,step):#####arguments are index of rows 
		
		row_arraylist = []

		for i in range(start,end,step):
			row_arraylist.append(np.array(array2d[i]))
		row_array= np.array(row_arraylist)
		return row_array
			
				

####################################################################################

########Generate a new array contains a specific column #########
	def extract_column(self,idx): ###argument idx is the number of colunms that to be extracted
		colarray = array2d[:,idx].reshape(5,idx)
		return colarray

####################################################################################

# ############generate a new array that contains the elements in the rectangular section [1,0],[3,2]###
 	def extract_rect(self,x1,y1,x2,y2): #arguments are the coordinates given
 		rectangularList = []
 		eleList = []
 		for row in range(x1,(x2+1)):
 			for col in range(y1,(y2+1)):
 				
 				ele = array2d[row][col]
 				rectangularList.append(ele)
 				rectarray = np.array(rectangularList)
 		return rectarray

####################################################################################

# #####Generate a new array that contains only elements with values that are between 3 and 11####
	def extract_specificval(self,lower,upper):#argument are the specific values given
		upperarray = array2d[np.where(array2d>lower)]
		specificvalarray = upperarray[np.where(upperarray<upper)]

		return specificvalarray
#####################################################################################

#######mannual test############
# a = create2Darray()
# print len(a.generate(15,5,3))

# # # x = a.extract_rows(1,4,2)
# # # rowarray = np.array([np.array([2,7,12]),np.array([4,9,14])])
# # # if x.all() != rowarray.all():
# # # 	print 'what the fuck'
# print a.extract_column(1)
# print a.extract_rect(1,0,3,2)
# print a.extract_specificval(3,11)
# print a.extract_specificval(3,11)
		