import re

def patternCount(genome, pattern):
    '''
    Solve the Pattern Count problem.

    Input: Strings Text and Pattern

    Output: Count(Text, Pattern)
    '''
    return len(re.findall(('(?=' + re.escape(pattern)) + ')', genome))
