from random import randint
from textblob import TextBlob
import sys

class MarkovKey:
    def __init__(self, key):
        self.key = key
        self.tags = ""

    def __str__(self):
        return self.key

    def __repr__(self):
        return self.key

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key

class MarkovVal:
    def __init__(self, word, weight):
        self.word = word
        self.tag = ""
        self.weight = weight

    def __str__(self):
        return self.word

    def __repr__(self):
        return self.word
        
    def setWeight(self, weight):
        self.weight = weight

class Markov:
    def __init__(self, corpus_path):
        self.corpus = open(corpus_path, 'r')
        self.corpusSize = self.getCorpusSize(corpus_path)
        self.markov = self.generateMarkov()

    def getCorpusSize(self, corpus_path):
        with open(corpus_path) as f:
            return sum(1 for _ in f)   

    def generateMarkov(self):
        sys.stdout.write("Step 1: Generating Markov Chain\n")
        sys.stdout.flush()
        tempStr = self.corpus.readlines()
        i = 0;
        for line in tempStr:
            i+=1
            sys.stdout.write("reading line " + str(i) + " of " + str(self.corpusSize) + "\r")
            sys.stdout.flush()
            blob = TextBlob(line)
            for idx, val in enumerate(blob.tags):
                sect = blob.tags[idx]
                if idx + 2 < len(blob.tags):
                    sect2 = blob.tags[idx+1]
                    value = blob.tags[idx+2]
                    keyStr = MarkovKey(sect[0] + " " + sect2[0])
                    keyStr.tags = sect[0][0] + " " + sect2[0][0]
                    valueStr = MarkovVal(value[0], 0.1)
                    valueStr.tag = value[0][0]
                    if 'markov' in locals():
                        if keyStr in markov:
                            markov[keyStr].append(valueStr)
                        else:
                            markov[keyStr] = [valueStr]
                    else:
                        markov = {keyStr: [valueStr]}
        return markov
'''
            #generates a 2 key markov chain
            for ind, word in enumerate(tempStrArr):
                
                #if the value does not exceed the array sixe
                if ind + 2 < len(tempStrArr):
                    keyStr = MarkovKey(tempStrArr[ind] + " " + tempStrArr[ind+1])
                    valueStr = MarkovVal(tempStrArr[ind + 2], 1)
                    
                    #if there is a variable called markov in the local scope
                    if 'markov' in locals():
                        #if the key already exists add it to value array
                        if keyStr in markov:
                            markov[keyStr].append(valueStr)
                        else:
                            markov[keyStr] = [valueStr]
                    else:
                        markov = {keyStr: [valueStr]}
        return markov'''

        
m = Markov('nietzsche.txt')
print(m.markov)
'''                
print(tempStr)
print("-------------------------------------------------------------------------")
print(markov)
'''
