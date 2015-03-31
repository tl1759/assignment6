##############################################
# Programming for Data Science Spring 2015   #
# Assignment 6								 #
# Practicing Numpy Based on Lecture 7 Slides #
#											 #
# Author: Lily Fung							 #
# Date: March 30, 2015						 #
#											 #
# Objective: To practice using numpy package #
#											 #
##############################################

import numpy as np

# Question 1: ################################

def question1():
	# Create the initial array

	q1_array = np.array([[1,  6, 11],
 					 	 [2,  7, 12],
 						 [3,  8, 13],
 						 [4,  9, 14],
 						 [5, 10, 15]])

	# a: Generate a new array containing the 2nd and 4th rows #
	q1a_array = np.array([q1_array[1], q1_array[3]])

	# b: Generate a new array that contains the 2nd column
	q1b_array = np.array([q1_array[:, 1]])

	# c: Generate a new array that contains all the elements in the rectangular section between the coordinates [1,0] and [3,2]
	q1c_array = np.array([q1_array[1:3, 0:2]])

	#d: Generate a new array that contains only elements with values that are between 3 and 11
	q1d_array = [element for element in q1_array.flat if (element >= 3 and element <= 11)]

	print "Question 1 \n", q1_array, "\n"
	print "Question 1a \n", q1a_array, "\n"
	print "Question 1b \n", q1b_array, "\n"
	print "Question 1c \n", q1c_array, "\n"
	print "Question 1d \n", q1d_array, "\n"

def question2():

	# Arranges an array a with elements 0 to 24 in a 5x5 grid
	a = np.arange(25).reshape(5,5)
	b = np.array([1., 5, 10, 15, 20])

	# Print directly the division of the two arrays
	print "Question 2 \n", a/b, "\n"

def question3():
	# Generate a 10 x 3 array of random numbers between [0,1]
	q3_array = np.random.rand(10,3)
	print "Question 3 \n", q3_array, "\n"

	# Find the index of the number closest to 0.5 in each row
	q3_index_array = np.array([ closest_to_05(row)for row in q3_array ])

	print "Indices of Numbers Closest to 0.5 \n", q3_index_array, "\n"

	# Use index array to extract those numbers and put into new array
	final_list = []
	loop_index = 0
	while loop_index < len(q3_index_array):
		final_list.append(q3_array[loop_index, q3_index_array[loop_index]])
		loop_index += 1
	q3_final_array = np.array(final_list)

	print "Numbers Closest to 0.5 \n", q3_final_array, "\n"

# Helper function for problem 3 which decides which number is closest to 0.5 by creating a temporary list which calculates distance from 0.5 and picks minimum of the 3
def closest_to_05(array_row):
	temp_list = []
	for element in array_row:
		temp_list.append(abs(element-0.5))
	return temp_list.index(min(temp_list))

"""Confusion about Question 4 directions -- not sure what we are being asked to do"""
# def question4():
# 	grid = np.array([-2,1], [-1.5, 1.5])

# 	N_max = 50
# 	some_threshold = 50

# 	c = x + 1j*y
# 	z = c
# 	for v in range(N_max):
# 		z = z**2 + c

# Unit Tests #

if __name__ == "__main__":
	# Question 1:
	question1()

	# Question 2:
	question2()

	# Question 3:
	question3()
