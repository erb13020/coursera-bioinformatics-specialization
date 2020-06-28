#Solve the Reverse Complement problem

#Input: A DNA string Pattern
#Output: Patternrc , the reverse complement of Pattern

def reverseComplement(genome):
    genome = genome[::-1] #reverse text
    genome = genome.upper() #ensure text is uppercase

    nucleotide = { #dictionary for finding complements for nucleotides
        'A':'T',
        'T':'A',
        'G':'C',
        'C':'G'
    }

    complement = [] #variable to hold result

    for n in genome:
        complement.append(nucleotide[n])

    return ''.join(complement)