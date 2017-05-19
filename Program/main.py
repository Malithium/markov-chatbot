from random import randint
import nltk
from nltk.tag import pos_tag, map_tag
import json
import sys

class MarkovKey:
    def __init__(self, key):
        self.key = key
        self.tags = ""

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.key == other.key
        else:
            return self.key == other

    def __ne__(self, other):
        return not(self.key, other.key)


class MarkovVal:
    def __init__(self, word, weight):
        self.word = word
        self.tag = ""
        self.weight = weight

    def __hash__(self):
        return hash(self.word)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.word == other.word
        else:
            return self.word == other
        
    def setWeight(self, weight):
        self.weight = weight
        print("Weight is now: " + str(weight))
    
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
        markov = {}
        for line in tempStr:
            i+=1
            sys.stdout.write("reading line " + str(i) + " of " + str(self.corpusSize) + "\r")
            sys.stdout.flush()
            strLine = str(line.lower().strip())

            text = nltk.word_tokenize(strLine)
            posTagged = pos_tag(text)
            simplifiedTags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in posTagged]
            
			#iterate over the result to get the individual words and tags
            for idx, val in enumerate(simplifiedTags):
                sect = simplifiedTags[idx]
                if idx + 1 < len(simplifiedTags):
                    sect2 = simplifiedTags[idx+1]
                    
					#the key value must consist of 2 words
                    keyStr = MarkovKey(sect[0] + " " + sect2[0])
                    keyStr.tags = sect[1] + " " + sect2[1]
                    
					#the value is the word following the second key value
                    leng = len(simplifiedTags)
                    if leng > 2 and idx+2 <= leng-1:
                        value = simplifiedTags[idx+2]
                        valueStr = MarkovVal(value[0], 1)
                        valueStr.tag = value[1]
                    else:
                        valueStr = MarkovVal("", 1)
                        valueStr.tag = ""

                    if len(markov) > 0:
                        if keyStr in markov:
                            markov[keyStr].append(valueStr)
                        else:
                            markov[keyStr] = [valueStr]
                    else:
                        markov = {keyStr: [valueStr]}
						
        #return the generated markov chain
        return markov
