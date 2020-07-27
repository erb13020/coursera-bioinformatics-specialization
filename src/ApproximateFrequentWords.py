import itertools
from collections import defaultdict


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
