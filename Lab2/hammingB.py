#!/usr/bin/python

#Lab 2 Question 1 B

#Hamming code

#Write a program to find out the code word for the given data word using Hamming code at the sender side


import sys
from math import *
import random


while(goodToGo==0):
	binary_string = '0110100111'#input("Enter binary string (of length 10) or code word (of length 14): ") #input works as raw_import for python 3.x 
	if len(binary_string) == 10 or len(binary_string) == 14:
		goodToGo = 1
		print('Good to go')
	else:
		print('Length of 10 or 14 only')


hamming_array = []
numOnes = -1

def isEven(binary_substr):
	global numOnes
	numOnes = 0
	for char in binary_substr:
		if char == '1':
			numOnes +=1
	if numOnes%2 == 0:
		#print("True, number of ones = ", numOnes)
		return True
	else:
		#print("False, number of ones = ", numOnes)
		return False



for char in binary_string:
	raw_array.append(char)

#insert random error
errorBit = floor(random.random()*10+1)
print('Error created at bit: ',errorBit)
print('Before:',raw_array[errorBit])
if raw_array[errorBit] =='0':
	raw_array[errorBit] ='1'
else:
	raw_array[errorBit] ='0'
print('After:',raw_array[errorBit])

for x in range(0, 14):
	hamming_array.append('null')
	
print('\n\nBefore populating:\n',hamming_array)
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
lazy = hamming_array[11] + hamming_array[12] + hamming_array[13] 
if (isEven(lazy)):
	hamming_array[7] = '0'
else:
	hamming_array[7] = '1'

#calc bit 4
lazy = hamming_array[6] + hamming_array[8] + hamming_array[9] + hamming_array[10]
if (isEven(lazy)):
	hamming_array[3] = '0'
else:
	hamming_array[3] = '1'

#calc bit 2
lazy = hamming_array[4] + hamming_array[5] + hamming_array[9] + hamming_array[10] + hamming_array[13]
if (isEven(lazy)):
	hamming_array[1] = '0'
else:
	hamming_array[1] = '1'

#calc bit 1
lazy = hamming_array[2] + hamming_array[5] + hamming_array[8] + hamming_array[10] + hamming_array[12]
if (isEven(lazy)):
	hamming_array[0] = '0'
else:
	hamming_array[0] = '1'

print('\nCode Word:\n', hamming_array)
print('Parity bits added:', hamming_array[0], hamming_array[1], hamming_array[3], hamming_array[7])

		


