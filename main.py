import string
import random

def gen_pass(size = 8, 
chars = string.ascii_letters + 
string.digits + 
string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))
	
if __name__ == "__main__":
	while True:
		size = input("Cuántos caracteres debe tener la contraseña? (Por defecto: 8) ")
		
		if not size.isdigit() and size == '':
			password = gen_pass()
			break
		elif size != '' and size.isdigit():
			size = int(size)
			password = gen_pass(size)
			break
	
	print(password)