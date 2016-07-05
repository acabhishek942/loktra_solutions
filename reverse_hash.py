import itertools

def reverse_hash(hashed):
	letters="acdegilmnoprstuw"

	the_string=""

	for i in itertools.count():
		if hashed==7:
			return the_string

		pos=hashed%37

		if pos < len(letters):
			the_string=letters[pos]+the_string
		else:
			return "Incorrect hash received"
			
		hashed=(hashed-pos)/37
		


print reverse_hash(680131659347)
print reverse_hash(930846109532517)