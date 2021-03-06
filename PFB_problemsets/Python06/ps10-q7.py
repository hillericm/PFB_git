#!/usr/bin/env python3


class dna_entry(object):

	#define class attributes
	def __init__(self,gene_name, sequence, gene_species):
		#allow class attributes to be defined from outside the class
		self.gene_name = gene_name
		self.sequence = sequence
		self.gene_species = gene_species

	#define length method
	def length(self):
		length = len(self.sequence)
		return length

	#define method that calculates nucleotide composition
	def nt_composition(self):
		countA = self.sequence.count('A')
		countC = self.sequence.count('C')
		countG = self.sequence.count('G')
		countT = self.sequence.count('T')
		return {'A': countA, 'C': countC, 'G': countG, 'T': countT}

	#define method for calculating GC content
	def GC_content(self):
		countGC = self.sequence.count('G') + self.sequence.count('C')
		finalGC = (countGC/len(self.sequence))*100
		return finalGC

	
	#define fasta formatter
	def fasta_format(self):
		finalfasta = ('>{}\t{}\n{}'.format(self.gene_name, self.gene_species, self.sequence))
		return finalfasta

dna_entry_obj = dna_entry(gene_name = 'notum', gene_species = 'Homo sapiens', sequence = 'AGTGTGTATGATAGTA')

print(dna_entry_obj)
print(dna_entry_obj.gene_name)
print(dna_entry_obj.sequence)
print(dna_entry_obj.gene_species)
print(dna_entry_obj.length())
print(dna_entry_obj.nt_composition())
print(dna_entry_obj.GC_content())
print(dna_entry_obj.fasta_format())
