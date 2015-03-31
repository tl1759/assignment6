import numpy as np
import matplotlib.pyplot as plt

#Question 1
# use numpy arrays to create the first 2-D array

print ""
print "Printing results for Question 1"
print ""

x = (np.arange(15).reshape(3,5) +1).transpose()
print x

a = np.array([x[1],x[3]])
print a

b = x[:,1].reshape(5,1)
print b

c = x[1:4,0:3]
print c

d = x[np.where(x>3)]
print d[np.where(d<11)]


#Question 2

print ""
print "Printing results for Question 2"
print ""

a2 = np.arange(25).reshape(5,5)
# you have to reshape the array that will be used as the divident 
b2 = np.array([1.,5,10,15,20]).reshape(5,1) 

Q2_result = a2/b2
print Q2_result


#Question 3

print ""
print "Printing results for Question 3"
print ""

# create the 10x3 array of random numbers in the range [0,1]
Q3_random = np.random.rand(10,3)
print Q3_random

#create an array that can be used to compare which numbers are closest to 0.5
diff = np.absolute(Q3_random-0.5)

# takes the index of the numbers with the smallest absolute difference 
print Q3_random[np.where((diff - diff.min(axis=1).reshape(10,1))==0)]


#Question 4

print ""
print "Saving results for Question 4"
print ""

# create a Mandelbrot fractal
N_max = 50
some_threshold = 2

x = np.linspace(-2, 1, 1000)
y = np.linspace(-1.5, 1.5, 1000)

# make an array that matches the x,y grid, since we want to store the img
final_array = np.zeros((len(x),len(y)), np.int) 

# start a loop that will create the grid needed and will check all the conditions
for i, x0 in enumerate(x):
	for j, y0 in enumerate(y):
		c = x0 + 1j*y0	# keep the initial value 
		z = c 		#value to be incremented

		for k in range(N_max):
			z = z**2 +c
			#check for the condition given in the question
			# changed the threshold given in the question and the operand so that the points that need to be bounded are included
			if np.absolute(z) > some_threshold:
				final_array[i, j] = k 
				break
		else:
			final_array[i, j] = 0

plt.imshow(final_array.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('mandelbrot_maha.png')
