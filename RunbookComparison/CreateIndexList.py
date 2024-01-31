# This is a script that will organize all of the runbooks in the README.md file into a list
# https://github.com/IBM/itz-support-public/blob/main/IBM-Technology-Zone/README.md?plain=1
import os

def CreateIndexList(filename):
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
        
        # remove the base path from each filename
        filteredList = [os.path.basename(link.strip('()')) for link in indexList]

        return filteredList


