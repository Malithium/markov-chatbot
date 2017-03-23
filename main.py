from random import randint

class MarkovVal:
	def __init__(self, word, weight):
		self.word = word
		self.weight = weight
		
	def setWeight(self, weight):
		self.weight = weight

class Markov:

	def __init__(self, corpus_path):
		self.corpus = open(corpus_path, 'r')
		self.markov = self.generateMarkov()
		
	def generateMarkov(self):
		tempStr = self.corpus.readlines()
		for line in tempStr:
			tempStrArr = line.split();
			#generates a 2 key markov chain
			for ind, word in enumerate(tempStrArr):
				
				#if the value does not exceed the array sixe
				if ind + 2 < len(tempStrArr):
					keyStr = tempStrArr[ind] + " " + tempStrArr[ind+1]
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
		return markov
		
	def createResponse(self, text):
		sentence = ""
		currKey = ""
		inputs = text.split()
		for i, w in enumerate(inputs):
			currKey = inputs[i] + " " + inputs[i+1]
			break;

		if currKey in self.markov:
			sentence = currKey
			while True:
				values = self.markov[currKey]
				val = values[randint(0,len(values)-1)]
				newKey = currKey.split()[1] + " " + val.word
				sentence += " " + val.word
				currKey = newKey
				if newKey not in self.markov:
					break
		print(sentence)
		
m = Markov('test.txt')
m.createResponse('I am')
print(m.markov)
'''				
print(tempStr)
print("-------------------------------------------------------------------------")
print(markov)
'''