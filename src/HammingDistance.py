import numpy as np


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
