#Implement the ClumpFind algorithm on the genome of E Coli

from lib import PatternMatch as pm, FrequentWords as fw
import time

e_coli_genome = 'resources/E_coli.txt'

def clumpFind(k, L, t):
    startTime = time.perf_counter()
    with open(e_coli_genome, 'r') as file:
        genome = file.read()
        results = []
        for start in range(len(genome)):
            print(str(start/len(genome)))
            cut = genome[start:L]
            matches = fw.frequentWords(cut, k)
            for pattern in matches:
                if(len(pm.patternMatch(pattern, cut)) == t):
                    if(pattern not in results):
                        results.append(pattern)
            L = L + 1
    endTime = time.perf_counter()
    print(endTime)
    return results