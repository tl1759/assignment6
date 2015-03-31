import unittest
from create2Darray import create2Darray as crt
import numpy as np
###################This part is the test fixture############################
array = np.array([np.array([1,6,11]),np.array([2,7,12]),np.array([3,8,13]),np.array([4,9,14]),([5,10,15])])
rowarray = np.array([np.array([2,7,12]),np.array([4,9,14])])
colarray = np.array([np.array([6,7,8,9,10])])
rectarray = np.array([2,7,8,12,13,14])
specvalarray = np.array([3,4,5,6,7,8,10,11])
crt().generate(15,5,3)
# c = ab.generate(1,12,5)
##################################################################################
class testcreate2Darray(unittest.TestCase):
	
	def testgenerate(self):
		self.assertEqual(crt().generate(15,5,3).all(),array.all(),'Array is not correctly created.')
	# def testextract_rows(self):
	# 	self.assertEqual(crt().extract_rows(1,4,2).all,rowarray.all(),'Please find out why it happens ')
	def testextract_column(self):
		self.assertEqual(crt().extract_column(1).all(),colarray.all(),'djkjfdk')
	def testextract_rect(self):
		self.assertEqual(crt().extract_rect(1,0,3,2).all(),rectarray.all(),'betternot appear')
	def textextract_specificval(self):
		self.assertEqual(crt().extract_specificval(3,11).all,specvalarray.all(),'this must not right')



unittest.main()