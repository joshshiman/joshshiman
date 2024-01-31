# Ensure that you have the prerequisites indicated in the README.md document

from CreateIndexList import CreateIndexList
from CreateAllList import CreateAllList

RunbookAppendix = CreateIndexList('RunbookIndex.txt')
RunbookRepository = CreateAllList('AllRunbooks.txt')


# check if runbook is missing from index
MissingRunbooks = []
for runbook in RunbookRepository:
    if runbook not in RunbookAppendix:
        print(f'{runbook} is missing from the Runbook Index')
        MissingRunbooks.append(runbook)

