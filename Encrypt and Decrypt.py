alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
	    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
	    'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
	    'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
		' ', '.']
		
new_alphabet = []

def encrypt(alphabet, letter):
	temp_num = alphabet.index(letter)
	x = 0
	while x < 5:
		temp_num += 1
		x += 1
		if temp_num == len(alphabet):
			temp_num = 0

	return alphabet[temp_num]
	
def decrypt(alphabet, letter):
	temp_num = alphabet.index(letter)
	x = 0
	while x > 0:
		temp_num -= 1
		x += 1
		if temp_num == 0:
			temp_num = len(alphabet)
	
	return alphabet[temp_num]

z = 0
for letter in alphabet:
	new_alphabet.append(encrypt(alphabet, alphabet[z]))
	z += 1

def encrypt_option():
	word = input("Type a word to encrypt: ")

	temp_str = ''
	number_list = []

	for letter in word:
		if letter in alphabet:
			number_list.append(alphabet.index(letter))

	for number in number_list:
		temp_str += str(new_alphabet[number])
	
	print("Word in numbers: '" + str(number_list) + "'")
	print("Word in plain text: '" + str(word) + "'")
	print("Word in encypted text: '" + str(temp_str) + "'\n\n")
	
def decrypt_option():
	word = input("Type a string to be decrypted: ")
	
	temp_str = ''
	number_list = []
	
	for letter in word:
		number_list.append(new_alphabet.index(letter))
			
	for number in number_list:
		temp_str += str(alphabet[number])
		
	print("Word in numbers: '" + str(number_list) + "'")
	print("Word in encrypted text: '" + str(word) + "'")
	print("Word in plain text: '" + str(temp_str) + "'\n\n")

def Main():
	RUNNING = True
	
	while RUNNING:
		option = input("Would you like to 'encrypt', 'decrypt', or 'quit'? ").lower()
		if option == 'encrypt':
			print('')
			encrypt_option()
		elif option == 'decrypt':
			print('')
			decrypt_option()
		elif option == 'quit':
			python.quit()
		else:
			print("I'm sorry, that wasn't an option, try again.\n\n")
			Main()
			
if __name__ == "__main__":
	Main()