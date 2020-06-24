import PatternCount as pc

#Solve the Frequent Words Problem
#Input: A string Text and an integer k
#Output: All most frequent k-mers in Text

def frequentWords(text, k):
    counts = [pc.patternCount(text, text[x:x + k]) for x in range(len(text) - k)]
    return set([text[x:x + k] for x in range(len(text) - k) if counts[x] == max(counts)])