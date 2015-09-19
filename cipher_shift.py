
def cipher_shift(in_letter, shift):
	# guard clause for non-alphanumerics
	if not in_letter.isalpha():
		return in_letter

	# determine the amount to shift in the ascii table
	if in_letter.isupper():
		alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if in_letter.islower():
		alphabet = "abcdefghijklmnopqrstuvwxyz"

	# shift the letter 
	base = alphabet.find(in_letter)
	new =  (base + shift) % 26
	return alphabet[new]



cipher = "Fraq hf gur pbqr lbh hfrq gb qrpbqr guvf zrffntr"

for key in range(25):
	out = ""
	for i in cipher:
		out = out + cipher_shift(i, key)
	print out + " \n"
