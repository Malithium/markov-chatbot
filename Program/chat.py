import json
import random
from random import randint

class chatBot:
    def __init__(self, fileName):
        self.brain = self.openFile(fileName)
        self.start = ""
        self.follow = ""
    
    def openFile(self, fileName):
        with open(fileName) as data_File:
            return json.load(data_File)
    
    def checkIntent(self, message):
        # TODO: Move this functionality to the JSON file to avoid repeating code
        # read in the templates from our brain file
        for temp in self.brain["Templates"]:
            if temp["Intent"] == "Greeting":
                if "hello" in message:
                    numOfKeys = len(temp["Keys"])
                    randomNm = randint(0,numOfKeys-1);
                    return temp["Keys"][randomNm]
            elif temp["Intent"] == "Age":
                if "old" in message:
                    numOfKeys = len(temp["Keys"])
                    randomNm = randint(0,numOfKeys-1);
                    return temp["Keys"][randomNm]
            elif temp["Intent"] == "State":
                if "feel" in message:
                    numOfKeys = len(temp["Keys"])
                    randomNm = randint(0,numOfKeys-1);
                    return temp["Keys"][randomNm]
            elif temp["Intent"] == "Name":
                if "name" in message:
                    numOfKeys = len(temp["Keys"])
                    randomNm = randint(0,numOfKeys-1);
                    return temp["Keys"][randomNm]
            elif temp["Intent"] == "Reality":
                if "real" in message:
                    numOfKeys = len(temp["Keys"])
                    randomNm = randint(0,numOfKeys-1);
                    return temp["Keys"][randomNm]
            elif temp["Intent"] == "Hobby":
                if "hobby" in message:
                    numOfKeys = len(temp["Keys"])
                    randomNm = randint(0,numOfKeys-1);
                    return temp["Keys"][randomNm]
            elif temp["Intent"] == "Appearance":
                if "look" in message:
                    numOfKeys = len(temp["Keys"])
                    randomNm = randint(0,numOfKeys-1);
                    return temp["Keys"][randomNm]
            

    def getWeightedValue(self, values):
        
        # sum up all of the weights for our values
        total = sum(val["Weight"] for val in values)
        
        # get a random value between 0 and the total sum
        r = random.uniform(0, total)
        upto = 0
        for value in values:
            
            # if upto + the weight of the value surpasses the random number generated return the value
            if upto + value["Weight"] >= r:
                return value["Word"]
            upto += value["Weight"]

    def generateMessage(self, sentence):
        
        # iterate over each chain in our markov chain
        for chain in self.brain["MarkovChain"]:
            if sentence is not None:
                
                # split up the parsed in sentence by whitespace
                words = sentence.split(" ")
                
                # if the length of our words array is greater than 1 then we have a valid sentence to build
                if len(words) > 1:
                    
                    # retrieve the key from the end of the word
                    if chain["Key"] == words[len(words)-2] + " " + words[len(words)-1]:
                        
                        # retrieve a value based on its weight
                        value = self.getWeightedValue(chain["Values"])                
                        self.follow += " " + value                
                        newKey = words[len(words)-1] + " " + value
                        
                        # call this function recursively until there is no valid key to build
                        self.generateMessage(sentence + " " + value)

    def chat(self):
        print("Type a message to the bot")
        inp = input()
        while inp != "":
            self.start = ""
            self.follow = ""
            key = self.checkIntent(inp)
            if key is not None:
                self.start = key
            self.generateMessage(key)
            print("ChatBot: " + self.start + self.follow)
            inp = input()