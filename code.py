# Lab Exercise 5

def computeDeBruijn2x4(deBruijnCurrentValues_2_4) :
    # Using polynomial x^4 + x + 1

    a = deBruijnCurrentValues_2_4[0]
    b = deBruijnCurrentValues_2_4[1]
    c = deBruijnCurrentValues_2_4[2]
    d = deBruijnCurrentValues_2_4[3]

    deBruijnOutput_2_4 = d

    feedback = (d+c)%2
    if a==0 and b==0 and c==0 and d==1 :
        feedback = 0
    elif a==0 and b==0 and c==0 and d==0 :
        feedback = 1

    deBruijnCurrentValues_2_4 = (feedback,a,b,c)

    return (deBruijnOutput_2_4,deBruijnCurrentValues_2_4)

def computeDeBruijn5x4(deBruijnCurrentValues_5_4) :
    # Using polynomial x^4 + 3x^3 +3x^2 + 2

    a = deBruijnCurrentValues_5_4[0]
    b = deBruijnCurrentValues_5_4[1]
    c = deBruijnCurrentValues_5_4[2]
    d = deBruijnCurrentValues_5_4[3]

    deBruijnOutput_5_4 = d

    feedback = (2*d + 3*b + 3*a)%5
    if a==0 and b==0 and c==0 and d==1 :
        feedback = 0
    elif a==0 and b==0 and c==0 and d==0 :
        feedback = 2

    deBruijnCurrentValues_5_4 = (feedback,a,b,c)

    return (deBruijnOutput_5_4,deBruijnCurrentValues_5_4)

def computeDigit(deBruijnOutput_2_4, deBruijnOutput_5_4) :
    digit = 5*deBruijnOutput_2_4+deBruijnOutput_5_4
    return digit

def checkIfDebruijnSequence(digitsString) :
    tuplePresent = []
    for digitIndex in range(0,len(digitsString)-3) :
        currentTuple = (digitsString[digitIndex],digitsString[digitIndex+1],digitsString[digitIndex+2],digitsString[digitIndex+3])
        tuplePresent.append(currentTuple)
    return len(set(tuplePresent))==10000


if __name__ == "__main__" :
    
    DE_BRUIJN_2_4_INITIAL_VALUES = (0,0,0,1)
    DE_BRUIJN_5_4_INITIAL_VALUES = (0,0,0,1)

    digitsString = ""
    deBruijnCurrentValues_2_4 = DE_BRUIJN_2_4_INITIAL_VALUES
    deBruijnCurrentValues_5_4 = DE_BRUIJN_5_4_INITIAL_VALUES

    for digitId in range(10003) :

        (deBruijnOutput_2_4,deBruijnCurrentValues_2_4) = computeDeBruijn2x4(deBruijnCurrentValues_2_4)
        (deBruijnOutput_5_4,deBruijnCurrentValues_5_4) = computeDeBruijn5x4(deBruijnCurrentValues_5_4)

        digitOutput = computeDigit(deBruijnOutput_2_4, deBruijnOutput_5_4)
        digitsString += str(digitOutput)

    file_name = "digits.txt"
    with open(file_name, 'w') as file:
        file.write(digitsString)

    isDeBruijnSequence = checkIfDebruijnSequence(digitsString)
    print(isDeBruijnSequence)