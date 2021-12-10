from my_functions import readthis
from pprint import pprint

beginningCharacters = ['(','[','M','<']
endingCharacters = [')',']','N','>']

lines = readthis('2021aoc10.txt','\n')

pointValue = {')' : 1,
              ']' : 2,
              'N' : 3,
              '>' : 4}

points = 0

badlines = []

for line in lines:
    bc = []
    ec = []
    for i in range(len(line)):
        if line[i] in beginningCharacters:
            bc.append(line[i])
        elif line[i] in endingCharacters:
            ec.append(line[i])
        if line[i] in endingCharacters:
            if beginningCharacters.index(bc[-1]) != endingCharacters.index(ec[-1]):
                badlines.append(line)
                break
            else:
                del bc[-1]
                del ec[-1]

goodlines = []

for line in lines:
    if line not in badlines:
        goodlines.append(line)

pprint(goodlines)

symbolstoadd = []

for j in range(len(goodlines)):
    i = 0
    while ('()' in goodlines[j]) or ('[]' in goodlines[j]) or ('MN' in goodlines[j]) or ('<>' in goodlines[j]):
        if goodlines[j][i:i+2] == '()' or goodlines[j][i:i+2] == '[]' or goodlines[j][i:i+2] == 'MN' or goodlines[j][i:i+2] == '<>':
            goodlines[j] = goodlines[j][:i] + goodlines[j][i+2:]
            i = 0
        if i > len(goodlines[j]) - 1:
            i = -1
        i += 1


pprint(goodlines)

characterstoadd = []

for line in goodlines:
    currentline = ''
    for char in line[::-1]:
        if char == '[':
            currentline += ']'
        elif char == 'M':
            currentline += 'N'
        elif char == '<':
            currentline += '>'
        else:
            currentline += ')'
    characterstoadd.append(currentline)
    

print(characterstoadd)

scores = []

for item in characterstoadd:
    score = 0
    for char in item:
        score *= 5
        score += pointValue[char]
    scores.append(score)
print(scores)
scores.sort()
print(scores)
print(scores[len(scores) // 2])


            
        
