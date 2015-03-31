# -*- coding: utf-8 -*-
###################################
#  Tae Kim
#
#  assignment6.py 
#  March 31,2015
#
#  various numpy exercises
#
###################################


import numpy as np
import matplotlib.pyplot as plt


def addNum(one, two, three):    
    """
    Create 2-D array 5 rows of 3 (one, two, three) numbers - increment of 1
    """
    numList=[]
    for item in xrange(5):
        addThis=[one+item,two+item, three+item]          #increment of 1
        numList.append(addThis)
    return numList                            


def separator():  
    """
    Separate between answers for easy readability 
    """
    print ""
    print "*"*25
    print ""
    return None


def numberOne(one, two, three):
    """
    various numpy exercises
    """
    
    # create array by calling addNum
    thisArray = np.array(addNum(one, two, three))   #thisArray will be used for number 1 question
    separator()
    print "Array to be used for problem 1."
    print thisArray                         
    separator()
    
    # Problem 1 A  - Generate a new array containing the 2nd and 4th rows
    print "Answer 1a"
    oneA = thisArray[np.array([1,3])]
    print oneA
    separator()

    # Problem 1 B  - Generate a new array that contains the 2nd column
    print "Answer 1b"
    oneB = thisArray[:, 1]
    print oneB
    separator()
 
    # Problem 1 C - Generate a new array that contains all the elements in the rectangular 
    #                 section between the coordinates ​[1,0]​and ​[3,2]
    print "Answer 1c"
    oneC = thisArray[1:4, 0:3]
    print oneC
    separator()
 
    # Problem 1 D - Generate a new array that contains only elements with values that are between 3 and 11
    print "Answer 1d"
    oneC = np.where((3<=thisArray[:]) & (thisArray[:]<=11))  #oneC will store index of values that are between 3 and 11
    print sorted(thisArray[oneC])    #sorted incrementally
    separator()


def numberTwo(one, two, three):   
    """
    divides each column element­wise with the array
    """
    print "Answer 2"
    thisArrayTwo = np.arange(one).reshape(two, three)      #array one=25, two=5, three=5
    division = np.array([1., 5, 10, 15, 20])
    divisionT = np.array(division)[np.newaxis].T         #transpose to divides each column element­wise with the array
    resultTwo = np.divide(thisArrayTwo,divisionT)        #divide  
    print resultTwo
    separator()


def listMaker(one, two, three):
    """
     receives three values and return a list after abs and -5
    """
    oneABS = abs(one-0.5)     #absolute value of the first value - 0.5
    twoABS = abs(two-0.5)      #absolute value of the second value - 0.5
    threeABS = abs(three-0.5)     #absolute value of the third value - 0.5
    tempList=[oneABS, twoABS, threeABS]          #store three into tempList
    return tempList


def numberThree(a,b):
    """
    generate a 10 x 3 array of random numbers in the range
    """
    
    threeArray = np.random.rand(a,b)    #a=10, b =3
    
    #Problem 3 A  - For each row, pick the number closest to 0.5
    print "Answer 3a"  
    threeAList=[]
    for item in threeArray:
        thisIndex = np.argmin(listMaker(item[0],item[1],item[2]))         #used argmin to find index of the lowest value
        threeAList.append(item[thisIndex])         #add value into list
        print item[thisIndex], "is the closest to 0.5 out of", item      #these are random values
    print ""
    print "1­D array--->", threeAList  #1D array of the numbers from each row closes to 0.5
    separator()    

    # Problem 3 B and 3 C
    print "Answer 3b and 3c"
    threeCList=[]
    for line in threeArray:
        thisIndex = np.argsort(listMaker(line[0],line[1],line[2]))            #np.argsort sorts the tempList by its value
        columnIndex = thisIndex[0]
        print "Column", int(columnIndex), "has the closest to 0.5 out of", line
        threeCList.append(line[columnIndex])
    print ""
    print "1­D array--->", threeCList
    separator()
    return threeAList,threeCList


# Problem 4 A
def numberFour(a,b,c,d,N_max, some_threshold):
    """
    Write a module that computes the Mandelbrot fractal using the Mandelbrot iteration
    """
    
    x,y= np.ogrid[a:b:200j,c:d:200j]  #Constructing a grid of ​c = x + 1j*y​values in the range ​[­2, 1] x [­1.5, 1.5]
                                      #higher the number
    c = x + 1j*y                 #code given
    z=c
    for v in xrange(N_max):     #Do the iteration
         z = z**2 + c               # this gives  RuntimeWarning: overflow encountered in square.  
                                    # sent TA an email to ask.  He replied that the value exceeding the capacity of an int
    if np.abs(z).all() < some_threshold:    #A point ​(x,y)​belongs to the Mandelbrot set if ​abs(z) < some_threshold
         mask = np.abs(z) 
    else:
         pass
#    
    plt.imshow(mask.T,extent=[-2,1,-1.5,1.5])
    plt.gray()
    plt.show()
    plt.savefig('mandelbrot.png')           #Save the result to an image 



if __name__ == "__main__":
    numberOne(1,6,11)
    numberTwo(25,5,5)
    numberThree(10,3)
    numberFour(-2, 1, -1.5, 1.5, 50, 50)


