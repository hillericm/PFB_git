#!/usr/bin/env python3
H4_wheat = '''AGCAC----CCTCCCACCTCATCCCACCCTTCTGATCTCAATCCAACG-TCG-----------CATCTCCACCGTCTCGC
-GGATCGACCCAG----CGAAGTCCCTC--CCGCC--CCCAAAGTCCC--------CCAAATCTTGCAGT-TCCCTCCTA
AATCCTCCCCA----TATAAACC-------AA---CCCCC-CGCCCTCAGATCCCTAATCCCA--------TCGCAAGC-
ATCAGACTCCCTC---C-AAAGCAG---GCA--------------GCAGCTCCTC-TTCTTCCTAATCACACTATCTCGG
AGAG-------------------------GAGCGGCCATGTCTGGGCGCGACAAGGGCGGCAAGGGGCTGGGCAAGGGCG
GCGCCAAGCGGCACCGGAAGGTCCTCCGCGACAACATCCAGGGCATCACCAAGCCGGCGATCCGGAGGCTGGCCAGGAGG
GGCGGCGTGAAGCGCATCTCCGGCCTCATCTACGAGGAGACCCGCGGCGTCCTCAAGATCTTCCTCGAGAACGTCATCCG
CGACGCCGTCACCTACACCGAGCACGCCCGCCGCAAAACCGTCACCGCCATGGACGTCGTCTACGCGCTCAAGCGCCAGG
GCCGCACCCTCTACGGCTTCGGAGGCTAGA---TTTGT--------GTGGTGAAGCAA----CTTCCTCGT---TTGCTC
TGTGATCTGTGC---TGTCGTAGATGAGATTTAC-TGATTT--------------GGCGTGCGCCGGTTGTATTCTGTCA
TGGGGTTCA-----GTGGGCTGTGTAATACCTTGCTCTGTACTTCTGTTCAATGCAATCACTT-CTATTCTGAA'''


H4_human = '''TCTAGAGATGGCGCCATTTGATTCCAGCAGCCACAAAGCACTAGAACAATCGATGCTAAGAGGTGACAGGAAAAACAGGC
TGCAAAGACCCAGACAATGGAATGCAGCGGTGGTCAGCCTAAAACACTGTAGAAGGGCAAGATGAGCTGAGTAATTTTTA
ACTGGGCATCATTTTTAGAAACTGGAGTTTAAGTACCCCCTTTTCCATTTTTTCCTGAAGTCGTGGGCAGGGCGCAAGGT
CTGTGAATCGGCCGACCGGATGCAGCTGGTGTGGAGAGTTCCCAATCAGGTCCGATTTATTACTATATAAAGTACTGCTG
CGAGGCTTGCCGTGTTGCATTTTGTTTAGTACAAGACATGTCTGGGCGCGGCAAAGGCGGGAAGGGTCTGGGCAAAGGAG
GCGCTAAGCGCCACCGCAAAGTTCTGCGCGACAACATTCAGGGCATCACCAAGCCCGCCATCCGACGCCTGGCACGGCGT
GGAGGCGTTAAGCGCATCTCAGGCCTTATATACGAGGAGACACGCGGAGTTCTTAAAGTGTTTTTGGAGAATGTAATCCG
CGATGCAGTTACCTACACGGAGCACGCCAAACGCAAGACAGTCACAGCCATGGACGTGGTTTACGCGCTCAAGCGCCAGG
GCCGCACCCTGTATGGCTTTGGCGGCTGAGTGTTTTACTTACTTACACGGTTCCTCAAAGGCCCTTCTCAGGGCCACCCA
TGAAGTCTGTGAAAGAGCTGTAGACTAAAGATAGTTAATTTCTTAAGAACACTTAAACGTATGGCAGTTTTGGCAAATTA
GCGATTCCACATAAGCAGTCGCTGAAGTTTGAGGTTCGGTGCCCCT-TTCA--GC-ATTACTTAGTGGTTAAAA'''

wheat_list = list(H4_wheat)
human_list = list(H4_human)

wheat_it = iter(wheat_list)
human_it = iter(human_list)

matches = 0
nonmatches = 0

for N in wheat_it:
	if N == human_it:
		matches += 1
	else:
		nonmatches += 1

print(matches, nonmatches)




print(type(H4_wheat))