def word_count(phrase):
	trom = dict()
	for i in phrase.split():
		if i in trom:
			trom[i] += 1 
		else:
			trom[i] = 1
	return trom