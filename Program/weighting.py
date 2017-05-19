from textBuilder import TextBuilder

class chatBotChain:    
    def __init__(self, templates, markov):
        self.templates = templates
        self.markov = markov

class finalTemplate:
    def __init__(self, intent, keys):
        self.intent = intent
        self.keys = keys

    def json(self):
        return dumps({'intent': self.intent, 'keys': self.keys})

def applyWeights(file):
    Templates = []
    t = TextBuilder(file)
    print("stage 3: Apply weights to values")
    keyCollection = []
    newMarkovList = []
    for approvedTemp in t.generatedText:
        keyCollection = []
        for sentence in approvedTemp.sentences:
            ind1 = 0
            ind2 = 1
            value = 2
            words = sentence.split(" ")
            cKey = words[ind1] + " " + words[ind2]
            while value <= len(words) - 1:
                key = words[ind1] + " " + words[ind2]
                for markovvalue in t.markov.markov[key]:
                    if markovvalue.word == words[value]:
                        markovvalue.setWeight(99)
                    
                ind1 = ind1 + 1
                ind2 = ind2 + 1
                value = value + 1
            keyCollection.append(cKey)
        Templates.append(finalTemplate(approvedTemp.template, keyCollection))
    cbChain = chatBotChain(Templates, t.markov.markov)
    return cbChain
    '''
    json_string = json.dumps([ob.__dict__ for ob in toJSON.templates])
    json_string2 = json.dumps([ob.__dict__ for ob in toJSON.markov])
    print(json_string)
    print(json_string2)
    with open("brain.json", "w") as outfile:
        json.dump(toJSON, outfile)
'''