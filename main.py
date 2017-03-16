tempStr = "There is a cat with a big hat and there are some dogs with tight collars there are also mice with long tails"
tempStrArr = tempStr.split();

#generates a 2 key markov chain
for ind, word in enumerate(tempStrArr):
    
    #if the value does not exceed the array sixe
    if ind + 2 < len(tempStrArr):
        keyStr = tempStrArr[ind] + " " + tempStrArr[ind+1]
        valueStr = tempStrArr[ind + 2]
        
        #if there is a variable called markov in the local scope
        if 'markov' in locals():

            #if the key already exists add it to value array
            if keyStr in markov:
                markov[keyStr].append(valueStr)
            else:
                markov[keyStr] = [valueStr]
        else:
            markov = {keyStr: [valueStr]}

print(tempStr)
print("-------------------------------------------------------------------------")
print(markov)
