# Frequent Words Problem
#
# Find the most frequent k-mers in a string.
#
# Input: A string Text and an integer k.
#
# Output: All most frequent k-mers in Text
#
# 10/20/2014


def FrequentWords(text, k, t):
    FrequentPatterns = set()
    vec_cont = []   
        
    for i in range(len(text)-k+1):
        count = 0
        pattern = text[i:i+k]
        for l in range(len(text)-k+1):
            compara = text[l:l+k]
            if pattern == compara:
                count += 1
        vec_cont.append(count)
         
    for i in range(len(text)-k+1):   
        if vec_cont[i] >= t:
            control = text[i:i+k]
            FrequentPatterns.add(control)
    return FrequentPatterns 
    

def ReadInput(dataset):
    data = []
    
    with open(dataset, "r") as input_data:
        #c = input_data.read(1)
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

#text = 'ATCAGACACTACCATATCAGACATTATAAACCAGAGTACCAGAGTACCAGAGTATCAGACACCAGAGTACTACCATCCGCCATAGCCGCCATAGCCGCCATAGCCGCCATAGCCGCCATAGACCAGAGTCCGCCATAGACTACCATCCGCCATAGATCAGACATCAGACATCAGACATTATAAATCAGACACCAGAGTACCAGAGTATTATAAACTACCATATTATAAACTACCATACTACCATATTATAACCGCCATAGATCAGACACCAGAGTCCGCCATAGACTACCATATTATAAACTACCATACTACCATATCAGACATTATAAATCAGACATCAGACCCGCCATAGATTATAAATCAGACATCAGACATCAGACACTACCATATTATAAATTATAAACTACCATATCAGACCCGCCATAGACCAGAGTATCAGACACTACCATATTATAAATTATAAACCAGAGTCCGCCATAGACCAGAGTATCAGACATCAGACATTATAAACTACCATATCAGACACCAGAGTCCGCCATAGCCGCCATAGATCAGACCCGCCATAGATCAGACATCAGACCCGCCATAGATCAGACATTATAAATCAGACATCAGACACTACCATACCAGAGTACCAGAGTCCGCCATAGCCGCCATAGATCAGACACCAGAGTACTACCATACCAGAGTACCAGAGTATCAGACACCAGAGTACCAGAGTATCAGACACTACCATATTATAACCGCCATAGATCAGACACCAGAGTATCAGACATTATAAACTACCATATTATAAACTACCATATCAGACACCAGAGTATCAGACATCAGACACTACCATATTATAACCGCCATAG'
k = 5
t = 4
print 'palabras mas frecuentes de', k ,'letras:'

WriteOutput(FrequentWords(ReadInput("dataset.txt"), k, t))
