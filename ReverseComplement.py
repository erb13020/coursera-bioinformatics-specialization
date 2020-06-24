#Solve the Reverse Complement problem

#Input: A DNA string Pattern
#Output: Patternrc , the reverse complement of Pattern

def reverseComplement(text):
    text = text[::-1] #reverse text
    text = text.upper() #ensure text is uppercase

    nucleotide = { #dictionary for finding complements for nucleotides
        'A':'T',
        'T':'A',
        'G':'C',
        'C':'G'
    }

    complement = [] #variable to hold result

    for n in text:
        complement.append(nucleotide[n])

    return ''.join(complement)