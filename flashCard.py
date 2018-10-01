# Author: Petras Swissler
# 2018-10-01
############################################
# Flash Card Giver
############################################
# Import Libraries
from random import randint
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
    
    sumScores = 0;

    #determine which definition to ask
    defAsk = randint(0,len(scores)-1)

    
    # Ask the definition
    print(definitions[defAsk])
    input("press any key to see answer")
    print(terms[defAsk])
    
    
    if (input("Did you answer Correctly? (y = yes):")=='y'):
        scores[defAsk] = scores[defAsk] - 1
    else:
        scores[defAsk] = scores[defAsk] + 1

        # Remove if never need to ask again
        if (scores[defAsk] <= 0):
            scores.remove(defAsk)
            terms.remove(defAsk)
            definitions.remove(defAsk)
    
    numRemainAsk = sum(scores);
    print("Num Remaining: ",numRemainAsk)
print("All Done")
