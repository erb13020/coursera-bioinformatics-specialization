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
