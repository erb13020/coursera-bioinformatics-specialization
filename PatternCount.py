import re

#Input: Strings Text and Pattern
#Output: Count(Text, Pattern)

def patternCount(text, pattern):
    return len(re.findall(('(?=' + re.escape(pattern)) + ')', text))
