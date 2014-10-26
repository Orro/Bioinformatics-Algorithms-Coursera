# Pattern Matching Problem
#
# Find all occurrences of a pattern in a string.
#
# Input: Two strings, Pattern and Genome.
#
# Output: All starting positions where Pattern appears as a substring of Genome.
#
# 10/26/2014

def findPattern(pattern, genome):
    indeces = set()
    b = genome.find(pattern)
    indeces.add(b)
    
    for i in range(len(genome)):
        if genome.find(pattern, i+1) != -1:
            indeces.add(genome.find(pattern, i))
    return sorted(indeces)        
        
###############################################################

#genome = 'GATATATGCATATACTT'
#pattern = 'ATAT'
pattern = 'CTTGATCAT'

data = []
file_name = "dataset.txt"

with open(file_name, "r") as genome:
    #c = genome.read(1)
    count = 0
    while True:
        c = genome.read(1)
        if c != '\n':
            data.append(c)
        if not c:
            break    

genome = ''.join(str(e) for e in data)


b =  findPattern(pattern, genome)
#print 'indeces', b

indeces = open("index.txt", "w")

for item in b:
    #print item
    indeces.write(" %s" % item)

indeces.close()
