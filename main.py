import re
import numpy as np

def patternMatch(genome, pattern):
    '''
    Pattern Matching Problem: Find all occurrences of a pattern in a string.

    Input: Strings Pattern and Genome.

    Output: All starting positions in Genome where Pattern appears as a substring.
    '''
    match_index = []
    end = len(pattern)
    for start in range(len(genome)):
        cut = genome[start:end]
        end = end + 1
        if (cut == pattern):
            match_index.append(start)
        else:
            pass
    return match_index

def frequentWords(genome, k):
    '''
    Solve the Frequent Words Problem

    Input: A string Text and an integer k

    Output: All most frequent k-mers in Text
    '''
    counts = [patternCount(genome, genome[x:x + k]) for x in range(len(genome) - k)]
    return set([genome[x:x + k] for x in range(len(genome) - k) if counts[x] == max(counts)])

def patternCount(genome, pattern):
    '''
    Solve the Pattern Count problem.

    Input: Strings Text and Pattern

    Output: Count(Text, Pattern)
    '''
    return len(re.findall(('(?=' + re.escape(pattern)) + ')', genome))

def reverseComplement(genome):
    '''
    Solve the Reverse Complement problem

    Input: A DNA string Pattern

    Output: Patternrc , the reverse complement of Pattern
    '''
    genome = genome[::-1]  # reverse text
    genome = genome.upper()  # ensure text is uppercase

    nucleotide = {  # dictionary for finding complements for nucleotides
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }

    complement = [] #variable to hold result

    for n in genome:
        complement.append(nucleotide[n])

    return ''.join(complement)

def clumpFind(genome, k, L, t):
    '''
        Clump Finding Problem: Find patterns forming clumps in a string.

             Input: A string Genome, and integers k, L, and t.

             Output: All distinct k-mers forming (L, t)-clumps in Genome.
    '''
    results = []
    for start in range(len(genome)):
        cut = genome[start:L]
        matches = frequentWords(cut, k)
        for pattern in matches:
            if (len(patternMatch(pattern, cut)) == t):
                if (pattern not in results):
                    results.append(pattern)
        L = L + 1
    return results

def skew(genome):
    '''
    Find the skew of a genome

    Input: String Genome

    Output: An array containing the skew from 5' to 3'
    '''
    genome = genome.upper()
    skew_values = {'A': 0, 'T': 0, 'C': -1, 'G': 1}
    skew = [0]
    for n in genome:
        skew.append(skew[-1] + skew_values[n])

    return skew

def minimumSkew(genome):
    '''
    Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.

    Input: A DNA string Genome.

    Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).
    '''
    skew_array = np.asarray(skew(genome))
    return np.where(skew_array == skew_array.min())[0]

def main():
    pass

if __name__ == "__main__":
    main()
