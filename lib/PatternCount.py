import re

#Input: Strings Text and Pattern
#Output: Count(Text, Pattern)

def patternCount(genome, pattern):
    return len(re.findall(('(?=' + re.escape(pattern)) + ')', genome))
