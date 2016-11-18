#!/usr/bin/python

#Lab 2 Question 1 A

#Hamming code

#Write a program to find out the code word for the given data word using Hamming code at the sender side


import sys
from math import *


binary_string = '1001101001'#input("Enter binary string (of 10 length): ") #input works as raw_import for python 3.x 

raw_array = []
hamming_array = []
numOnes = -1

def isEven(binary_substr):
	global numOnes
	numOnes = 0
	for char in binary_substr:
		if char == '1':
			numOnes +=1
	if numOnes%2 == 0:
		print("True, number of ones = ", numOnes)
		return True
	else:
		print("False, number of ones = ", numOnes)
		return False



for char in binary_string:
	raw_array.append(char)

for x in range(0, 14):
	hamming_array.append('null')
	
print('Before populating:\n',hamming_array)
try:
	#hamming_array[0] = 
	#hamming_array[1] = 
	hamming_array[2] = raw_array[0]
	#hamming_array[3] = 
	hamming_array[4] = raw_array[1]
	hamming_array[5] = raw_array[2]
	hamming_array[6] = raw_array[3]
	#hamming_array[7] = 
	hamming_array[8] = raw_array[4]
	hamming_array[9] = raw_array[5]
	hamming_array[10] = raw_array[6]
	hamming_array[11] = raw_array[7]
	hamming_array[12] = raw_array[8]
	hamming_array[13] = raw_array[9]

except Exception:
	print('I dont really care')

print('After populating:\n',hamming_array)

#calc bit 8 
lazy = hamming_array[8] + hamming_array[9] + hamming_array[10] + hamming_array[11] + hamming_array[12] + hamming_array[13]
if (isEven(lazy)):
	hamming_array[7] = '0'
else:
	hamming_array[7] = '1'

#calc bit 4


