# Elementary Cellular Automata
# Python v 2.7

ruleNum = int(raw_input("Rule number: "))
generations = int(raw_input("Number of Generations: "))
initSequence = "------------------------#------------------------"
initSequence = initSequence.replace("#", "1").replace("-", "0")

# Convert to 0s and 1s
ruleNum = str(bin(ruleNum)[2:])
ruleNum = ruleNum.zfill(8)
ruleNum = ruleNum[::-1]

ruleList = {}
i = 0
# Automatically create binary rule sets based off of input
while i < 8:
    for j in ruleNum:
        x = str(bin(i)[2:]).zfill(3)
        ruleList[x] = j
        i = i + 1


# Does the logic for calculating sequence
def runSequence(initSequence):
    j = 0
    endSeq = ""
    for x in initSequence:
        curVal = initSequence[j]
        if j == len(initSequence) - 1:  # Grab next value if at the end
            nexVal = initSequence[0]
        if j < (len(initSequence) - 1):
            nexVal = initSequence[j + 1]
        if j == 0:  # If at First position, grab last element
            befVal = initSequence[len(initSequence) - 1]
        befVal = initSequence[j - 1]
        for key, value in ruleList.items():
            if key == befVal + curVal + nexVal:
                endSeq = endSeq + value
        j = j + 1
    return endSeq


print initSequence.replace("1", "#").replace("0", "-")

# repeat till number of generations is completed
i = 0
while i < generations:
    endSeq = runSequence(initSequence)
    initSequence = endSeq
    i = i + 1
    print initSequence.replace("1", "#").replace("0", "-")
