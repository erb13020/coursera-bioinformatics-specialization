# coursera-bioinformatics-specialization
Python 3 code implementations of the bioinformatics algorithms presented in Coursera's Bioinformatics Specialization.

#Courses
- Finding Hidden Messages in DNA (Bioinformatics I). (In Progress)
- Genome Sequencing (Bioinformatics II).
- Comparing Genes, Proteins, and Genomes (Bioinformatics III).  
- Molecular Evolution (Bioinformatics IV).
- Genomic Data Science and Clustering (Bioinformatics V).  
- Finding Mutations in DNA and Proteins (Bioinformatics VI).

# Functions

| Algorithm         | Function                      | Input                                     | Output                                                                |
| ----------------  | ----------------------------- | ----------------------------------------- | --------------------------------------------------------------------- |
| Pattern Match     | patternMatch(genome, pattern) | Strings genome and pattern                | All starting positions in Genome where Pattern appears as a substring |
| Frequent Words    | freqeuntWords(genome, k)      | A string genome and an integer k          | All most frequent k-mers in Text                                      |
| Pattern Count     | patternCount(genome, pattern) | Strings genome and pattern                | Count(Text, Pattern)                                                  |
| Reverse Complement| reverseComplement(genome)     | A DNA string genome                       | genomerc , the reverse complement of genome                           |
| Clump Find        | clumpFind(genome, k, L, t)    | A string Genome, and integers k, L, and t | All distinct k-mers forming (L, t)-clumps in Genome.                  |
