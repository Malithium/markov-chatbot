from main import Markov
import nltk
from nltk.tag import pos_tag, map_tag
import json
import sys

class approvedTemp:
    def __init__(self, name, values):
        self.template = name
        self.sentences = values

class TextBuilder:
    def __init__(self, corpus_path):
        self.markov = Markov(corpus_path)
        self.templates = self.getTemplates()
        self.sampleSentences = []
        self.approvedSentences = []
        self.generatedText = self.textBuild()

    def getTemplates(self):
        sys.stdout.write("Step 2: retrieve templates\n")
        sys.stdout.flush()
        with open("templates.json") as temp_json:
            data = json.load(temp_json)
            return data["Templates"]

    def generateSignature(self, temp):
        signatures = []
        for response in temp:
            text = nltk.word_tokenize(response)
            posTagged = pos_tag(text)
            simplifiedTags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in posTagged]
            Str = ""
            for val, tag in simplifiedTags:
                Str += tag + " "
            Str.rstrip()
            print(Str)
            signatures.append(Str)
        return signatures

    def matchKey(self, sig):
        kTags = ""
        # retrieve the first 2 signature tags to form a key signature
        if len(sig.split(" ")) > 2:
            kTags = sig.split(" ")[0] + " " + sig.split(" ")[1]
        else:
            kTags = sig

        discoveredKeys = []
        for key in self.markov.markov:
            #check to see if the key tags match up with the start of the signature
            if key.tags == kTags:
                discoveredKeys.append(key)
        return discoveredKeys

    def generateSentences(self, mKeys, sig, ind):
        sentences = []
        for key in mKeys:
           sent = key.key
           sent = self.generateSentence(key, sig, sent, ind)
           if sent is not None and len(sent.split(" ")) == 3:
               self.sampleSentences.append(sent)
        return sentences
                    
    def generateSentence(self, key, signature, sentence, ind):
        newSent = sentence
        if len(newSent.strip().split(" ")) != len(signature.strip().split(" ")):
            for val in self.markov.markov[key]:
                newSent = sentence
                if val.word != "":
                    if ind <= len(signature) - 1:
                        if val.tag == signature.split(" ")[ind]:
                            newSent += " " + val.word

                            if len(newSent.strip().split(" ")) == len(signature.strip().split(" ")):
                                self.sampleSentences.append(newSent)

                            sentenceSize = len(newSent.split(" "))
                            if sentenceSize-2 > 0:
                                nxtKey = newSent.split(" ")[sentenceSize-2] + " " + newSent.split(" ")[sentenceSize-1]
                                result = self.generateSentence(nxtKey, signature, newSent, ind+1)
                                if result is not None:
                                    self.sampleSentences.append(result)

    def retrieveText(self, tempName, values):
        vals = values.split(" ")
        sentences = []
        if values != "":
            for val in vals:
                ival = int(val)
                sentences.append(self.sampleSentences[ival])
            
        apprved = approvedTemp(tempName, sentences)
        return apprved

    def textBuild(self):
        fTemps = []
        #Iterate over each template
        for temp in self.templates:
            self.sampleSentences = []

            #generate the response signatures
            signatures = self.generateSignature(temp["Responses"])

            for sig in signatures:
                mKeys = self.matchKey(sig)
                signatureLength = len(sig.strip().split(" "))

                if signatureLength > 2:
                    self.generateSentences(mKeys, sig, 2)
                else:
                    for key in mKeys:
                        self.sampleSentences.append(key.key)
                self.sampleSentences = list(set(self.sampleSentences))

            for ind, sentence in enumerate(self.sampleSentences):
                 print(ind, sentence)

            inp = input("input the index of each appropriate response to the " + temp["Type"] + " template\n")
            finalTemp = self.retrieveText(temp["Type"], str(inp))
            fTemps.append(finalTemp)
        return fTemps
