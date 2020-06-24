#Implement patternMatch algorithm on the genome of vibrio cholerae

import PatternMatch as pm

vibrio_genome = 'resources/Vibrio_cholerae.txt'

def patternMatchVibrioCholerae(pattern):
    with open(vibrio_genome, 'r') as file:
        genome = file.read()
        return pm.patternMatch(pattern, genome)