import re

def hey(what):
	
	what = what.strip()

	if what == "":
		return "Fine. Be that way!"

	elif what == what.upper() and re.search('[a-zA-Z]', what):
		return "Whoa, chill out!"

	elif what[-1] == '?':
		return "Sure."

	else:
		return "Whatever."
