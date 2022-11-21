def processInput():
    inputFile = open('rosalind_gc.txt')
    sequences = inputFile.readlines()
    i=1
    tempString=''
    inputStrings =[]
    while(i<len(sequences)):
        if(sequences[i].__contains__('>')):
            inputStrings.append(tempString)
            inputStrings.append(sequences[i])
            tempString=''
            i+=1
        elif (i == len(sequences) - 1):
            tempString+=sequences[i]
            inputStrings.append(tempString)
            i += 1
        else:
            tempString += sequences[i]
            i += 1
    inputStrings.insert(0,sequences[0])
    i=0
    while (i < len(inputStrings)):
        inputStrings[i] = inputStrings[i].replace('\n','')
        inputStrings[i] = inputStrings[i].replace('>','')
        i+=1
    return inputStrings

def gcontent(inputstrings):
    max_gc = 0
    for i in range(1,len(inputstrings),2):
        g = inputstrings[i].count('G')
        c = inputstrings[i].count('C')
        gc = ((g+c)/len(inputstrings[i]) )*100
        if gc>max_gc:
            max_gc = gc
            index = i
    print(inputstrings[index-1])
    print(max_gc)
    return max_gc,inputstrings[index-1]
gcontent(processInput())
