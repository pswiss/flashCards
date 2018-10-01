# Author: Petras Swissler
# 2018-10-01
############################################
# Flash Card Asker
############################################
# Import Libraries
from random import*

#Helper Functions
#https://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python/
def weighted_choice_sub(weights):
    rnd = random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i
            
# Define global variables
flashFile = "termsAndDefinitions.txt"

# Get how many times to default ask a term
numAsk = input ("Min Number of Times to Ask: ")

# Load in the flash card file into an array
lineNum = 0
terms = []
definitions = []
scores = []

with open(flashFile,'r') as fin:
    for line in fin:
        lineNum = lineNum+1

        tempString = line.split("|")

        terms.append(tempString[0])
        definitions.append(tempString[1])
        scores.append(int(numAsk))
            
# Loop until no entries remain
numRemainAsk = sum(scores);

while (numRemainAsk > 0):
    print("----------------------------------------")
    
    sumScores = 0;

    #determine which definition to ask
    #defAsk = randint(0,len(scores)-1)
    defAsk = weighted_choice_sub(scores)

    
    # Ask the definition
    print(definitions[defAsk])
   
    if(input("Input term: ")== terms[defAsk]):
        scores[defAsk] = scores[defAsk] - 1
        print("Correct! ",terms[defAsk])
    else:
        scores[defAsk] = scores[defAsk] + 1
        print("Incorrect! ",terms[defAsk])
    
    numRemainAsk = sum(scores);
    print("Num Remaining: ",numRemainAsk,"\r\n")
print("All Done")
