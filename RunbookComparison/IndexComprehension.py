# This is a script that will search for all of the runbooks that are not in the README.md file
# https://github.com/IBM/itz-support-public/blob/main/IBM-Technology-Zone/README.md?plain=1

with open('RunbookIndex.txt', 'r') as f:
    index = str(f.read())

    # initialize indexList
    indexList = []

    # initialize flags and runbook link
    lineStart = False
    lineEnd = False
    runbookLink = ""

    # loop to go through each line in the index
    for line in index:
    # if condition is reached set flags, remove previous flag, append runbook link to the list and reset runbook link
        if line == '(':
            lineEnd = False
            lineStart = True
        if line == ')':
            lineStart = False
            lineEnd = True
            indexList.append(runbookLink)
            runbookLink = ""

    # if lineStart flag is true, then add each new word to the runbook link.
        if lineStart == True:
            runbookLink += line



    print(indexList)