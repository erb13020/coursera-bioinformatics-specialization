from src import HammingDistance as hd

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
        if(hd.hammingDistance(cut, pattern) <= d):
            match_index.append(start)
        else:
            pass
    return match_index