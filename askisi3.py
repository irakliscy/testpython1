import requests
import json
from datetime import datetime

oddNumbers = []
evenNumbers = []
daysData = {}
numbersFreq = {}
bonusFreq = {}
oddFreq = {}
evenFreq = {}
totalEvenNumbersCounter = 0
totalOddNumbersCounter = 0
totalEvenWinningParity = 0
totalOddWinningParity = 0

for i in range(1, 80, 2):
    oddFreq[i] = 0
    evenFreq[i + 1] = 0

for i in range(1, 81, 1):
    numbersFreq[i] = 0
    bonusFreq[i] = 0

nowT = datetime.now()
currTime = nowT.strftime("%H:%M:%S")
currH = int(nowT.strftime("%H"))
currMin = int(nowT.strftime("%M"))

nowD = datetime.now()
currY = nowD.strftime("%Y")
currMonth = nowD.strftime("%m")
today = nowD.strftime("%Y-%m-%d")
daysElapsed = int(nowD.strftime("%d"))
if currH < 9:
    daysElapsed -= 1
elif currH == 9 and currMin < 5:
    daysElapsed -= 1

for i in range(daysElapsed):
    day = i + 1
    if day < 10:
        currD = f"{day}".format(day)
        fromDate = f"{currY}-{currMonth}-0{currD}".format(currY, currMonth, currD)
    else:
        currD = f"{day}".format(day)
        fromDate = f"{currY}-{currMonth}-{currD}".format(currY, currMonth, currD)
    toDate = fromDate

    gameId = 1100
    data = requests.get(f"https://api.opap.gr/draws/v3.0/{gameId}/draw-date/{fromDate}/{toDate}/draw-id".format(gameId, fromDate, toDate))
    datajson = data.json()
    firstDraw = datajson[0]
    moreData = requests.get(f"https://api.opap.gr/draws/v3.0/1100/{firstDraw}".format(firstDraw))
    wholeDataPackage = moreData.json()
    daysData[i] = wholeDataPackage['winningNumbers']

    for j in daysData[i]['list']:
        numbersFreq[j] += 1
        if j % 2 == 0:
            evenFreq[j] += 1
            totalEvenNumbersCounter += 1
        else:
            oddFreq[j] += 1
            totalOddNumbersCounter += 1

    currBonus = daysData[i]['bonus'][0]
    bonusFreq[int(currBonus)] += 1

    if daysData[i]['sidebets']['winningParity'] == 'even':
        totalEvenWinningParity += 1
    else:
        totalOddWinningParity += 1

maxNum = 0
maxNumKeys = []
maxBonus = 0
maxBonusKeys = []
for i in range(1, 81, 1):
    if numbersFreq[i] > maxNum:
        del maxNumKeys[:]
        maxNum = numbersFreq[i]
        maxNumKeys.append(i)
    elif numbersFreq[i] == maxNum:
        maxNumKeys.append(i)

    if bonusFreq[i] > maxBonus:
        del maxBonusKeys[:]
        maxBonus = bonusFreq[i]
        maxBonusKeys.append(i)
    elif bonusFreq[i] == maxBonus:
        maxBonusKeys.append(i)

print("The number(s) that appeared most frequently were: ", maxNumKeys, " and each of them appeared a total of ", maxNum, " times!")
print("\nThe bonus number(s) that appeared most frequently were: ", maxBonusKeys, " and each of them appeared a total of ", maxBonus, " times!" )

maxOdd = 0
maxEven = 0
maxOddKeys = []
maxEvenKeys = []
for i in range(1, 80, 2):
    if oddFreq[i] > maxOdd:
        del maxOddKeys[:]
        maxOdd = oddFreq[i]
        maxOddKeys.append(i)
    elif oddFreq[i] == maxOdd:
        maxOddKeys.append(i)

    if evenFreq[i + 1] > maxEven:
        del maxEvenKeys[:]
        maxEven = evenFreq[i + 1]
        maxEvenKeys.append(i + 1)
    elif evenFreq[i + 1] == maxEven:
        maxEvenKeys.append(i + 1)

print("\nThe odd number(s) that appeared the most were: ", maxOddKeys, "and appeared a total of ", maxOdd, " times! Also the total appearances of odds were: ", totalOddNumbersCounter)
print("\nThe even number(s) that appeared the most were: ", maxEvenKeys, "and appeared a total of ", maxEven, " times! Also the total appearancess of evens were: ", totalEvenNumbersCounter)

if totalOddWinningParity > totalEvenWinningParity:
    print("\nOdds were the winning parity more times than evens. Total times odds won: ",totalOddWinningParity)
elif totalOddWinningParity < totalEvenWinningParity:
    print("\nEvens were the winning parity more times than odds. Total times evens won: ",totalEvenWinningParity)
else:
    print("\nEvens and odds were the winning parity the same amount of times. Total times each parity won: ",totalOddWinningParity)
