# This is a script that will organize all of the runbooks in the GitHub repository into a list
# https://github.com/IBM/itz-support-public/tree/main/IBM-Technology-Zone/IBM-Technology-Zone-Runbooks


def CreateAllList(filename):
    # initialize indexList
    indexList = []

    # open file
    with open(f'RunbookComparison/{filename}', 'r') as f:
        index = str(f.read())

        # initialize flags and runbook link
        lineStart = False
        lineEnd = False
        runbookLink = ""

        # loop to go through each line in the index
        for line in index:
        # if condition is reached set flags, remove previous flag, append runbook link to the list and reset runbook link
            if line != '\n':
                lineEnd = False
                lineStart = True
            if line == '\n':
                lineStart = False
                lineEnd = True
                indexList.append(runbookLink)
                runbookLink = ""

        # if lineStart flag is true, then add each new word to the runbook link.
            if lineStart == True:
                runbookLink += line

        # create a new list containing only elements with '.md'
        filteredList = [runbook for runbook in indexList if '.md' in runbook]

        # create a new list with everything removed before each filename
        simpleList = []
        for runbook in filteredList:
            space_index = runbook.rfind(' ')
            if space_index != -1:
                runbookName = runbook[space_index + 1:].strip()
                simpleList.append(runbookName)

        # create a new list with no duplicates
        uniqueList = list(set(simpleList))

        return uniqueList
