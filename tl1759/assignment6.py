
##################################################################################
#########Liwen Tian
############Assignment6
############This is the main module to print other modules' outputs############




############################################################
import numpy as np 
from create2Darray import create2Darray as crt
from dividearray import dividearray
from find_nearest import find_nearest
from MandelbrotFractal import mandelbrot
import unittest
import sys

array = np.random.rand(10,3)
b = 0.5
def print_problem1():
	print "Question1's output is: \n", crt().generate(15,5,3),"\n"
	print "Question1a's output is: \n", crt().extract_rows(1,4,2),"\n"
	print "Question1b's output is: \n", crt().extract_column(1),"\n"
	print "Question1c's output is: \n", crt().extract_rect(1,0,3,2),"\n"
	print "Question1d's output is: \n", crt().extract_specificval(3,11),"\n"
def print_problem2():
	print "Question2's result is: \n",dividearray(),"\n"
def print_problem3():
	print "For question3, the nearest numbers are: \n",find_nearest(array,0.5),"\n"
def print_problem4():
	print "Question4's result is saved in the folder, please go check it.\n"
	mandelbrot(50,50)

###########################################################################

if __name__ =="__main__":
	print_problem1()
	print_problem2()	
	print_problem3()	
	print_problem4()
######################################test part####################
import test_create2Darray as test	
