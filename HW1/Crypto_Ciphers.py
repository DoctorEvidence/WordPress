__author__ = "Paolo Bondi: Classic Ciphers"
__date__ = "Aug 29, 2018"
__version__ = "1.0.0"


import random
import math
import time
import numpy as np
from numpy.linalg import inv

#ceaser cipher with 
#n = number of spaces to shift
#plaintext = message
def ceaser(string):
	def encrypt(n, plaintext):
		key = 'abcdefghijklmnopqrstuvwxyz'
		"""Encrypts and returns the cipher text"""
		result = ''

		for l in plaintext.lower():
			try:
				i = (key.index(l) + n ) % 26
				result += key[i]
			
			except ValueError:
				result += l

		return result.lower()

	def decrypt(n, ciphertext):
		key = 'abcdefghijklmnopqrstuvwxyz'
		"""Decrypt and returns the plain string"""
		result = ''

		for l in ciphertext:
			try:
				i = (key.index(l) - n) % 26
				result += key[i]

			except ValueError:
				result += l

		return result

	plaintext = string
	n = input("enter spaces to shift: ")

	encrypted = encrypt(n, plaintext)
	decrypted = decrypt(n, encrypted)

	print 'Rotated by: %s' % n
	print 'Plaintext: %s' % plaintext
	print 'Encrypted: %s' % encrypted
	print 'Decrypt: %s ' % decrypted

#substitution cipher
def Sub_cipher(string):
	alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
	key = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'
	plaintext = string

	def encrypt(plaintext, key, alphabet):
		keyIndices = [alphabet.index(k.lower()) for k in plaintext]
		return ''.join(key[keyIndex] for keyIndex in keyIndices)

	def decrypt(cipher, key, alphabet):
		keyIndices = [key.index(k) for k in cipher]
		return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)

	cipher = encrypt(plaintext, key, alphabet)

	print(plaintext)
	print(cipher)
	print(decrypt(cipher, key, alphabet))


#
#poly-alphabetical cipher
#
def Poly_alphabetical(string):
	encrypt_letter_to_num = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25,"'":26,",":27,".":28,"?":29,"/":30," ":31}
	encrypt_num_to_letter = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z",26:"'",27:",",28:".",29:"?",30:"/",31:" "}
	displacement_word = raw_input("please enter the displacement word: ")
	main_body = string

	def encrypt(displacement_word, main_body):
		displacement_list = []

		for x in displacement_word:
			displacement_list.append(encrypt_letter_to_num[x])

		displacement_list_position_count = 0
		new_word = ""

		for x in main_body:
			if displacement_list_position_count == len(displacement_list):
				displacement_list_position_count = 0
			old_value = encrypt_letter_to_num[x]
			new_value = old_value + displacement_list[displacement_list_position_count]
			while new_value > 31:
				new_value -= 32
			new_word += encrypt_num_to_letter[new_value]
			displacement_list_position_count += 1

		print("Encrypted word: " + new_word)
		decrypt(displacement_word, new_word);

	def decrypt(displacement_word, main_body):
		displacement_list = []
		for x in displacement_word:
			displacement_list.append(encrypt_letter_to_num[x])

		displacement_list_position_count = 0
		new_word = ""

		for x in main_body:
			if displacement_list_position_count == len(displacement_list):
				displacement_list_position_count = 0
			old_value = encrypt_letter_to_num[x]
			new_value = old_value - displacement_list[displacement_list_position_count]
			while new_value < 0:
				new_value += 32
			new_word += encrypt_num_to_letter[new_value]
			displacement_list_position_count += 1

		print("Unencrypted word: " + new_word)

	encrypt(displacement_word, main_body);

#
#tansposition cipher
#
def Trans_cipher(string):

	use = string
	

	def split_len(seq, length):
	    return [seq[i:i + length] for i in range(0, len(seq), length)]

	def encode(key, plaintext):

	    order = {
	        int(val): num for num, val in enumerate(key)
	    }

	    ciphertext = ''
	    for index in sorted(order.keys()):
	        for part in split_len(plaintext, len(key)):
	            try:
	                ciphertext += part[order[index]]
	            except IndexError:
	                continue

	    return ciphertext
    
    	print("coded message: " + encode('3214', use))
    	print("uncoded message: " + use)



#
#vigenere cipher
#
def vigenere_cipher(string):
	plaintext = string
	key = raw_input("enter the key to be used: ")

	def encrypt(plaintext, key):
	    key_length = len(key)
	    key_as_int = [ord(i) for i in key]
	    plaintext_int = [ord(i) for i in plaintext]
	    ciphertext = ''

	    for i in range(len(plaintext_int)):
	        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
	        ciphertext += chr(value + 65)
		
		print("encoded message: " + ciphertext)	

	    return decrypt(ciphertext, key);
	 
	 
	def decrypt(ciphertext, key):
	    key_length = len(key)
	    key_as_int = [ord(i) for i in key]
	    ciphertext_int = [ord(i) for i in ciphertext]
	    plaintext = ''
	    for i in range(len(ciphertext_int)):
	        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
	        plaintext += chr(value + 65)

	

	encrypt(plaintext, key)
	print("Unencrypted message: " + plaintext)

#main w/ cipher options & help
"""def main():
	while True:
		print("#")
		print("Welcome to my encryption program!")
		print("#")
		print("Your options are: vigenere, transpositional, poly-alphabetic, substitution, ceaser, help")
		answer = raw_input("")
		if answer == "vigenere":
			vigenere_cipher()
		elif answer == "transpositional":
			Trans_cipher()
		elif answer == "poly-alphabetic":
			Poly_alphabetical()
		elif answer == "substitution":
			Sub_cipher()
		elif answer == "ceaser":
			ceaser()
		elif answer == "help":
			print("your options are: vigenere, transpositional, poly-alphabetic, substitution, ceaser, help")
"""
def main():
	filename = raw_input("please enter the file you wish to encrypt")

	with open(filename, 'r') as myFile:
		data = myFile.read().replace('\n', '')
		print(data)
		print("#")
		print("Welcome to my encryption program!")
		print("#")
		
		print("Your options are: vigenere, transpositional, poly-alphabetic, substitution, ceaser, help")
		answer = raw_input("")
		if answer == "vigenere":
			vigenere_cipher(data)
		elif answer == "transpositional":
			Trans_cipher(data)
		elif answer == "poly-alphabetic":
			Poly_alphabetical(data)
		elif answer == "substitution":
			Sub_cipher(data)
		elif answer == "ceaser":
			ceaser(data)
		elif answer == "help":
			print("your options are: vigenere, transpositional, poly-alphabetic, substitution, ceaser, help")

main();


