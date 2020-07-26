from src import HammingDistance as hd


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
        if (hd.hammingDistance(cut, pattern) <= d):
            match_count = match_count + 1
        else:
            pass
    return match_count
