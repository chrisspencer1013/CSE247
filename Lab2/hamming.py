#!/usr/bin/python

#Lab 2 Question 1 A and B

#Hamming code

#Write a program to find out the code word for the given data word using Hamming code at the sender side


import sys
from math import *
import random

dataword_array = []
codeword_array = []
numOnes = -1
goodToGo=0 #bit to check if string is 10 or 14 chars long
randError = 1 #bit for turning on random error insertion

while(goodToGo==0):
	#binary_string = '0110100111'
	#binary_string = '11011101100111'
	binary_string = input("Enter binary string (of length 10) or code word (of length 14): ") #input works as raw_import for python 3.x 
	if len(binary_string) == 10 or len(binary_string) == 14:
		goodToGo = 1
	else:
		print('Length of 10 or 14 only')

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

if len(binary_string) == 10:
	print('\n\n\tPart A:\n')
	for char in binary_string:
		dataword_array.append(char)

	for x in range(0, 14):
		codeword_array.append('null')
		
	print('\n\nBefore populating:\n',codeword_array)
	try:
		#codeword_array[0] = 
		#codeword_array[1] = 
		codeword_array[2] = dataword_array[0]
		#codeword_array[3] = 
		codeword_array[4] = dataword_array[1]
		codeword_array[5] = dataword_array[2]
		codeword_array[6] = dataword_array[3]
		#codeword_array[7] = 
		codeword_array[8] = dataword_array[4]
		codeword_array[9] = dataword_array[5]
		codeword_array[10] = dataword_array[6]
		codeword_array[11] = dataword_array[7]
		codeword_array[12] = dataword_array[8]
		codeword_array[13] = dataword_array[9]
	except Exception:
		print('I dont really care')

	print('After populating:\n',codeword_array)




	#calc bit 8 
	lazy = codeword_array[11] + codeword_array[12] + codeword_array[13] 
	if (isEven(lazy)):
		codeword_array[7] = '0'
	else:
		codeword_array[7] = '1'

	#calc bit 4
	lazy = codeword_array[6] + codeword_array[8] + codeword_array[9] + codeword_array[10]
	if (isEven(lazy)):
		codeword_array[3] = '0'
	else:
		codeword_array[3] = '1'

	#calc bit 2
	lazy = codeword_array[4] + codeword_array[5] + codeword_array[9] + codeword_array[10] + codeword_array[13]
	if (isEven(lazy)):
		codeword_array[1] = '0'
	else:
		codeword_array[1] = '1'

	#calc bit 1
	lazy = codeword_array[2] + codeword_array[5] + codeword_array[8] + codeword_array[10] + codeword_array[12]
	if (isEven(lazy)):
		codeword_array[0] = '0'
	else:
		codeword_array[0] = '1'

	print('\nCode Word:\n', codeword_array)
	print('Parity bits added:', codeword_array[0], codeword_array[1], codeword_array[3], codeword_array[7])

if len(binary_string) == 14:
	print('\n\n\tPart B:\n')

	for char in binary_string:
		codeword_array.append(char)
	for x in range(0, 10):
		dataword_array.append('null')
	print(codeword_array)
	#insert random error
	if randError == 1:
		errorBit = floor(random.random()*13+1)
	
		#make sure it only hits the original binary string
		# if errorBit == 1:
		# 	errorBit = 2
		# elif errorBit == 2:	
		# 	errorBit = 4
		# elif errorBit == 3:
		# 	errorBit = 5
		# elif errorBit == 4:
		# 	errorBit = 6
		# elif errorBit == 5:
		# 	errorBit = 8
		# elif errorBit == 6:
		# 	errorBit = 9
		# elif errorBit == 7:
		# 	errorBit = 10
		# elif errorBit == 8:
		# 	errorBit = 11
		# elif errorBit == 9:
		# 	errorBit = 12
		# elif errorBit == 10:
		# 	errorBit = 13
		# else:
		# 	print('error')

		print('Error created at bit #: ',errorBit+1)
		print('Before error:',codeword_array[errorBit])
		if codeword_array[errorBit] =='0':
			codeword_array[errorBit] ='1'
		else:
			codeword_array[errorBit] ='0'
		print('After error:',codeword_array[errorBit])
		print(codeword_array)

	isEightCorrect = -1
	isFourCorrect = -1
	isTwoCorrect = -1
	isOneCorrect = -1

	#check parity bit 8
	lazy = codeword_array[7] + codeword_array[11] + codeword_array[12] + codeword_array[13] 
	if (isEven(lazy)):
		isEightCorrect = 1
		print('Bit 8 is correct')	
	else:
		isEightCorrect = 0
		print('Bit 8 is incorrect')

	#check parity bit 4
	lazy = codeword_array[3] + codeword_array[6] + codeword_array[8] + codeword_array[9] + codeword_array[10] 
	if (isEven(lazy)):
		isFourCorrect = 1
		print('Bit 4 is correct')
		
	else:
		isFourCorrect = 0
		print('Bit 4 is incorrect')

	#check bit 2
	lazy = codeword_array[1] + codeword_array[4] + codeword_array[5] + codeword_array[9] + codeword_array[10] + codeword_array[13] 
	if (isEven(lazy)):
		isTwoCorrect = 1
		print('Bit 2 is correct')
	else:
		isTwoCorrect = 0
		print('Bit 2 is incorrect')

	#check bit 1
	lazy = codeword_array[0]+ codeword_array[2] + codeword_array[5] + codeword_array[8] + codeword_array[10] + codeword_array[12]
	if (isEven(lazy)):
		isOneCorrect = 1
		print('Bit 1 is correct')
	else:
		isOneCorrect = 0
		print('Bit 1 is incorrect')

	print('isEightCorrect:',isEightCorrect)
	print('isFourCorrect:',isFourCorrect)
	print('isTwoCorrect:',isTwoCorrect)
	print('isOneCorrect:',isOneCorrect)

	if isOneCorrect == 1:
		if isTwoCorrect == 1:
			if isFourCorrect == 1:
				if isEightCorrect == 1:
					print('No errors detected')
				else:
					print('Error found at bit 8 or 12')
			else:
				if isEightCorrect == 1:
					print('Error found at bit 4 or 7')
				else:
					print('Error found at codeword[6 and 11?]')
		else:
			if isFourCorrect == 1:
				if isEightCorrect == 1:
					print('Error found at bit 2 or 5')
				else:
					print('Error found at bit 14')
			else:
				if isEightCorrect == 1:
					print('Error found at bit 10')
				else:
					print('Error found at codeword[idk]')
	else:
		if isTwoCorrect == 1:
			if isFourCorrect == 1:
				if isEightCorrect == 1:
					print('Error found at bit 1 or 3')
				else:
					print('Error found at bit 13')
			else:
				if isEightCorrect == 1:
					print('Error found at bit 9')
				else:
					print('Error found at codeword[]')
		else:
			if isFourCorrect == 1:
				if isEightCorrect == 1:
					print('Error found at bit 6')
				else:
					print('Error found at bit 8')
			else:
				if isEightCorrect == 1:
					print('Error found at bit 11')
				else:
					print('Error found at codeword[]')