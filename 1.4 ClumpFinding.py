# Clump Finding Problem
#
# Find patterns forming clumps in a string.
#
# Input: A string Genome, and integers k, L, and t.
#
# Output: All distinct k-mers forming (L, t)-clumps in Genome.
#
# 10/26/2014

def ComputingFrequencies(Text, k):
    FrequencyArray = []

    for i in range(4 ** k):
        FrequencyArray.append(0)

    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i+k]
        j = PatternToNumber(Pattern)
        FrequencyArray[j] = FrequencyArray[j] + 1
    return FrequencyArray        

def PatternToNumber(Pattern):
    if len(Pattern) == 0:
        return 0
    symbol = LastSymbol(Pattern)
    Pattern = Pattern[:-1]
    return 4 * PatternToNumber(Pattern) + int(SymbolToNumber(symbol))

def NumberToPattern(index, k):
    if k == 1:
        return NumberToSymbol(str(index))
    prefixIndex =  index / 4
    r = index % 4
    PrefixPattern = NumberToPattern(prefixIndex, k - 1)
    symbol = NumberToSymbol(str(r))
    return str(PrefixPattern) + str(symbol)

def NumberToSymbol(number):
    Num = {'0':'A', '1':'C', '2':'G', '3':'T'}
    
    return Num.get(number)
    
def LastSymbol(Pattern):
    return Pattern[-1] 

def SymbolToNumber(symbol):
    Sym = {'A':'0', 'C':'1', 'G':'2', 'T':'3'}
    return Sym.get(symbol)

def BetterClumpFinding(Genome, k, t, L):
        FrequentPatterns = set()
        Clump = []

        for i in range(4 ** k): 
            Clump.append(0)
        Text = Genome[0: L]
        FrequencyArray = ComputingFrequencies(Text, k)

        for i in range(4 ** k):
            if FrequencyArray[i] >= t:
                Clump[i] = 1

        for i in range(1, len(Genome) - L + 1):
            FirstPattern = Genome[i - 1: i - 1 + k]
            j = PatternToNumber(FirstPattern)
            FrequencyArray[j] = FrequencyArray[j] - 1
            LastPattern = Genome[i + L - k: i + L]
            j = PatternToNumber(LastPattern)
            FrequencyArray[j] = FrequencyArray[j] + 1
            if FrequencyArray[j] >= t:
                Clump[j] = 1

        for i in range(4 ** k):
            if Clump[i] == 1:
                Pattern = NumberToPattern(i, k)
                FrequentPatterns.add(Pattern)
        return FrequentPatterns
    
########################################################
data = []
file_name = "dataset.txt"
with open(file_name, "r") as Text:
    count = 0
    while True:
        c = Text.read(1)
        if c != '\n':
            data.append(c)
        if not c:
            break    

Text = ''.join(str(e) for e in data)

k = 4 
L = 30
t = 3

b = BetterClumpFinding(Text, k, t, L)

frec = open("output.txt", "w")
for item in b:
  frec.write(" %s" % item)
frec.close()  

    
