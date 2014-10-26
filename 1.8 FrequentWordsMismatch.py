# Frequent Words with Mismatches Problem
#
# Find the most frequent k-mers with mismatches in a string.
#
# Input: A string Text as well as integers k and d. (You may assume k <= 12 and d <= 3.)
#
# Output: All most frequent k-mers with up to d mismatches in Text.
#
#(Note that such k-mers do not need to actually appear as substrings of Text.)
#
# 10/26/2014

def WordsMismatch(genome, k, d):
    FrequentPatterns = set()
    vec_cont = []   
    
    for i in range(len(genome)-k+1):
        count = 0
        pattern = genome[i:i+k]
        for l in range(len(genome)-k+1):
            compara = genome[l:l+k]
            if HammingDistance(pattern, compara) <= d:
                count += 1
        vec_cont.append(count)
   
    t = max(vec_cont)
    
    for i in range(len(genome)-k+1):   
        if vec_cont[i] == t:
            control = genome[i:i+k]
            FrequentPatterns.add(control)
    return FrequentPatterns 
        
def HammingDistance(str1, str2):
    a = zip(str1, str2)
    count = 0
    
    for i in a:
        if i[0] != i[1]:
            count += 1
    return count

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
    
#############  I/O test  ######################################### 
k = 8
d = 2
WriteOutput(WordsMismatch(ReadInput("dataset.txt"), k, d))


     


