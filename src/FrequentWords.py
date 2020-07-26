from src import PatternCount as pc

def frequentWords(genome, k):
    '''
    Solve the Frequent Words Problem

    Input: A string Text and an integer k

    Output: All most frequent k-mers in Text
    '''
    counts = [pc.patternCount(genome, genome[x:x + k]) for x in range(len(genome) - k)]
    return set([genome[x:x + k] for x in range(len(genome) - k) if counts[x] == max(counts)])
