#!/usr/bin/env python3


class dna_entry(object):

	#define class attributes
	def __init__(self,gene_name, sequence, gene_species):
		#allow class attributes to be defined from outside the class
		self.gene_name = gene_name
		self.sequence = sequence
		self.gene_species = gene_species


dna_entry_obj = dna_entry(gene_name = 'notum', gene_species = 'Homo sapiens', sequence = 'AGTGTGTATGATAGTA')

print(dna_entry_obj)
print(dna_entry_obj.gene_name)
print(dna_entry_obj.sequence)
print(dna_entry_obj.gene_species)
