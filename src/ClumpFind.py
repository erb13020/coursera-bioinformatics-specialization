from src import PatternMatch as pm, FrequentWords as fw


def clumpFind(genome, k, L, t):
    '''
        Clump Finding Problem: Find patterns forming clumps in a string.

             Input: A string Genome, and integers k, L, and t.

             Output: All distinct k-mers forming (L, t)-clumps in Genome.
    '''
    results = []
    for start in range(len(genome)):
        cut = genome[start:L]
        matches = fw.frequentWords(cut, k)
        for pattern in matches:
            if (len(pm.patternMatch(pattern, cut)) == t):
                if (pattern not in results):
                    results.append(pattern)
        L = L + 1
    return results
