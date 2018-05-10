import itertools
import sys

def createPasswordList():
	"Creates a password list"
	with open('passwords.txt', 'w') as f:
		generator=itertools.combinations_with_replacement('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVW_.,;:!?ß[](){}/\%&$§"@€^°+-*', 15)
		for password in generator:
			f.write(''.join(password) + '\n')
		print ("Done")

createPasswordList()