def removed(letters, remove):
	for L in remove:
		letters = letters.replace(L, '', 1)
	return letters
