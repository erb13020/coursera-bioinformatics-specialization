import itertools
import re
from collections import defaultdict

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

def hammingDistance(s1, s2):
    '''
    Hamming Distance Problem: Compute the Hamming distance between two strings.

    Input: Two strings of equal length.

    Output: The Hamming distance between these strings.
    '''
    nucleotide_values = {'A': 1, 'T': 2, 'C': 3, 'G': 4}
    new_s1 = []
    new_s2 = []

    for n in range(len(s1)):
        new_s1.append(nucleotide_values[s1[n]])

    for n in range(len(s1)):
        new_s2.append(nucleotide_values[s2[n]])

    s1 = np.asarray(new_s1)
    s2 = np.asarray(new_s2)

    return (s1 != s2).sum()

def approximatePatternMatching(pattern, genome, d):
    '''
    Find all approximate occurrences of a pattern in a string.

    Input: Strings Pattern and Genome along with an integer d.

    Output: All starting positions where Pattern appears as a substring of genome with at most d mismatches.
    '''
    match_index = []
    end = len(pattern)
    for start in range(len(genome) - len(pattern) + 1):
        cut = genome[start:end]
        end = end + 1
        if(hammingDistance(cut, pattern) <= d):
            match_index.append(start)
        else:
            pass
    return match_index

def approximatePatternCount(genome, pattern, d):
    '''
    Find number of approximate occurrences of a pattern in a string.

    Input: Strings Pattern and Genome along with an integer d.

    Output: Count(Text, Pattern) with at most d mismatches.
    '''
    match_count = 0
    end = len(pattern)
    for start in range(len(genome) - len(pattern) + 1):
        cut = genome[start:end]
        end = end + 1
        if (hammingDistance(cut, pattern) <= d):
            match_count = match_count + 1
        else:
            pass
    return match_count


def approximateFrequentWords(genome, k, d):
    '''
    Find the most frequent k-mers with mismatches in a genome.

    Input: A string genome as well as integers k and d
    Output: All most frequent k-mers with up to d mismatches in genome
    '''

    def permuteMotifDistanceTimes(motif, d):
        workingSet = {motif}
        for _ in range(d):
            workingSet = set(itertools.chain.from_iterable(map(permuteMotifOnce, workingSet)))
        return list(workingSet)

    def permuteMotifOnce(motif, alphabet={'A', 'C', 'G', 'T'}):
        return list(set(itertools.chain.from_iterable([[
            motif[:pos] + nucleotide + motif[pos + 1:] for
            nucleotide in alphabet] for
            pos in range(len(motif))])))

    aprox_frq_words = []
    frequencies = defaultdict(lambda: 0)

    for index in range(len(genome) - k + 1):
        curr_kmer_and_neighbors = permuteMotifDistanceTimes(genome[index: index + k], d)
        for kmer in curr_kmer_and_neighbors:
            frequencies[kmer] += 1

    for kmer in frequencies:
        if frequencies[kmer] == max(frequencies.values()):
            aprox_frq_words.append(kmer)

    return aprox_frq_words


def main():
    pass


if __name__ == "__main__":
    main()
