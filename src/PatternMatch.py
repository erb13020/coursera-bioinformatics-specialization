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
