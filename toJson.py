from weighting import applyWeights
import json

def makeTemplatesJSONSeraible(templates):
    newTemps = []
    for temp in templates:
        newTemp = {}
        newTemp['Intent'] = temp.intent
        newTemp['Keys'] = temp.keys
        newTemps.append(newTemp)
    return newTemps

def makeMarkovJSONSeriable(markov):
    newMarkov = []
    for key in markov:
        values = markov[key]
        newValues = []
        for value in values:
            newVal = {}
            newVal['Word'] = value.word
            newVal['Weight'] = value.weight
            newValues.append(newVal)
        newKeyVal = {}
        newKeyVal['Key'] = key.key
        newKeyVal['Values'] = newValues
        newMarkov.append(newKeyVal)
    return newMarkov

def createMarkovChain(file):
    result = applyWeights(file)
    newMark = makeMarkovJSONSeriable(result.markov)
    newTemps = makeTemplatesJSONSeraible(result.templates)
    chatBotBrain = {}
    chatBotBrain["MarkovChain"] = newMark
    chatBotBrain["Templates"] = newTemps
    with open("brain.json", "w") as outfile:
        json.dump(chatBotBrain, outfile)
