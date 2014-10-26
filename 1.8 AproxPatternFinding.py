# Approximate Pattern Matching Problem
#
# Find all approximate occurrences of a pattern in a string.
#
# Input: Two strings Pattern and Text along with an integer d.
#
# Output: All positions where Pattern appears in Text with at most d mismatches.
#
# 10/26/2014

def AproxPatternFinding(pattern, genome, distance):
    indeces = []
    
    for i in range(len(genome)-len(pattern)+1):
        if  HammingDistance(pattern, genome[i:i+len(pattern)]) <= distance:
            indeces.append(i)
    return indeces

def HammingDistance(str1, str2):
    a = zip(str1, str2)
    count = 0
    
    for i in a:
        if i[0] != i[1]:
            count += 1
    return count

#############  I/O test  ######################################### 
def ReadInput(dataset):
    data = []
    
    with open(dataset, "r") as input_data:
        count = 0
        while True:
            c = input_data.read(1)
            if c != '\n':
                data.append(c)
            if not c:
                break    
    return ''.join(str(e) for e in data)
    
def WriteOutput(output):
    output_data = open("output.txt", "w")

    for item in output:
        output_data.write(" %s" % item)

    output_data.close()

pattern ='CAAGTATCA'
distance = 4 
WriteOutput(AproxPatternFinding(pattern, ReadInput("dataset.txt"),distance))
