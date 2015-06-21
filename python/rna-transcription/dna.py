from string import maketrans

def to_rna(strand):
	instrand = 'GCTA'
	outstrand = 'CGAU'

	trans = maketrans(instrand,outstrand)

	return strand.translate(trans)
#Disclaimer:
#i`ve done it before.. with Eduardo Borges,
#aka @eduardomrb 