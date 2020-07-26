import numpy as np

from src import Skew


def minimumSkew(genome):
    '''
    Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.

    Input: A DNA string Genome.

    Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).
    '''
    skew = np.asarray(Skew.skew(genome))
    return np.where(skew == skew.min())[0]
