#shifting strings
def shiftingStrings(string, leftShift, rightShift):
  diff = leftShift - rightShift
  if diff ==0 or len(string) ==1:
    return string
  elif diff > 0:
    temp = string[:diff]
    string = string[diff:]
    string += temp
    return string
  else:
    temp = string[:(len(string)-abs(diff))]
    string = string[(len(string)-abs(diff)):]
    string += temp
    return string

shiftingStrings("a", 0, 1)

# Separating Students
def minMoves(avgArr):
  #swapping all 1 to the left side
  countLeftToRight = 0
  zero = 0
  for i in range(len(avgArr)):
    if avgArr[i] == 0:
      zero += 1
    else:
      countLeftToRight += zero

  #swapping all 1 to the right side
  countRightToLeft = 0
  zero = 0
  for i in range(len(avgArr)-1, -1, -1):
    if avgArr[i] == 0:
      zero += 1
    else:
      countRightToLeft += zero

  return min(countLeftToRight, countRightToLeft)

minMoves([ 0, 0, 1, 0, 1, 0, 1, 1])

# Parking Delimma
def carParkingRoof(cars, k):
  minLength = 2147483647
  if k == len(cars):
    minLength = max(cars) - min(cars) +1
    return minLength

  cars.sort()
  i = 0
  while (i -1 +k ) < len(cars):
    minLength = min((cars[i+k-1] - cars[i] +1), minLength)
    i += 1
  return minLength

carParkingRoof([2, 6, 7, 12], 4)

# Large Responses
fileName = input()
text = open(fileName, "r")
readline = text.readline()

numOfRequests = 0
sumOfBytes = 0

while readline:
  oneBytes = int(readline.split(" ")[-1])
  if oneBytes > 5000:
    numOfRequests += 1
    sumOfBytes += oneBytes
  readline = text.readline()
  outFile = open("bytes_" + fileName, "w")
  outFile.write(str(numOfRequests) + "\n" + str(sumOfBytes) + "\n")
  text.close()
  outFile.close()

# Two Strings
def commonSubstring(str1, str2):
  i =0
  while i < len(str1):
    for j in range(len(str1[i])):
      if str1[i][j] in str2[i]:
        print("Yes")
        break
      if j == len(str1[i])-1:
        print("No")
    i += 1
commonSubstring(["hlelo", "hi", "cc"], ["woldf", "bye", "ef"])

# compression
def compressedString(inputStr):
  finalString = inputStr[0]
  counter = 1;
  for i in range(1, len(inputStr), 1):
    if inputStr[i] != inputStr[i-1]:
      if counter != 1:
        finalString += str(counter)
        counter = 1
      finalString += inputStr[i]
    if inputStr[i] == inputStr[i-1]:
      counter += 1
      if(i == len(inputStr)-1):
        finalString += str(counter)
  return finalString

compressedString("aaabffvfvf")

# Who's the closest
def closest(inputString, query):
  left = query -1
  right = query +1

  while left >=0 and inputString[left] != inputString[query]:
    left -=1
  
  while right <len(inputString)-1 and inputString[right] != inputString[query]:
    right +=1

  if inputString[left] == inputString[query] and (right >len(inputString)-1 or inputString[right] != inputString[query]):
    return left
  if (left < 0 or inputString[left] != inputString[query]) and inputString[right] == inputString[query]:
    return right
  if inputString[left] == inputString[query] and inputString[right] == inputString[query]:
    return right if query-left > right-query else left
  if inputString[left] != inputString[query] and inputString[right] != inputString[query]:
    return -1

closest("bababb", 5)

# partitioning array
import collections
def solve(k, numArr):
  if k ==1: 
    return "Yes"
  if k<=0 or k > len(numArr) or len(numArr)%k != 0: 
    return "No"
  groups = len(numArr)/k
  maxRepeat = collections.Counter(numArr)
  maxRepeat = max(maxRepeat.values())
  return "No" if maxRepeat > groups else "Yes"

solve(2, [1,2,2,2,3,3])

# Aladdin and his Carpet
def optimalPoint(magicArr, distArr):
  canFinishArr = [True for i in range(len(magicArr))]

  for i in range(len(magicArr)):
    totalMagic = 0
    visitedIndexArr = []

    j =i
    while j not in visitedIndexArr:
      visitedIndexArr.append(j)
      totalMagic = totalMagic + magicArr[j] - distArr[j]
      if totalMagic < 0:
        canFinishArr[i] = False
        break
      if j == len(magicArr)-1:
        j = 0
      else:
        j += 1
        
  print(canFinishArr)
  return canFinishArr.index(True) if True in canFinishArr else -1
      
optimalPoint([3,2,5,4], [2,3,6,4])

# Meandering Array
def meanderingArray(unsorted):
  unsorted.sort(reverse=True)
  # print(unsorted)

  half = len(unsorted)//2
  firstHalf = unsorted[:half+1]
  secondHalf = unsorted[half+1:]

  j =1
  for i in range(len(secondHalf)-1, -1, -1):
    firstHalf.insert(j, secondHalf[i])
    j += 2

  return firstHalf

print(meanderingArray([-1,1,2,3,-5]))
print(meanderingArray([7,5,2,7,8,-2,25,25]))

# Triplets
def triplets(threshold, arr):
  count =0

  if len(arr) < 3:
    return count
  arr.sort()
  
  for i in range(len(arr)-2):
    low = i+1
    high = len(arr)-1
    rest = threshold - arr[i]
    while low < high:
      if rest >= arr[low] + arr[high]:
        count += high - low
        low += 1
      else:
        high -= 1
  return count

triplets(7, [1,2,3,4,5])

# Purchasing Supplies
def maximumContainers(scenarios):
  ansArr =[]
  for scenario in scenarios:
    totalContainers = 0
    scenarioList = scenario.split(" ")
    buget = int(scenarioList[0])
    cost = int(scenarioList[1])
    m = int(scenarioList[2])

    containersFromBuy = buget // cost
    totalContainers += containersFromBuy

    containersFromReturn = totalContainers
    subTotalContainers = containersFromReturn
    while subTotalContainers >= m:
      containersFromReturn = subTotalContainers // m 
      totalContainers += containersFromReturn
      subTotalContainers = subTotalContainers // m + subTotalContainers % m
    
    ansArr.append(totalContainers)

  for containers in ansArr:
    print(containers)

maximumContainers(["10 2 5", "12 4 4", "6 2 2"])
maximumContainers(["8 4 2", "7 2 3"])

# merge 2 arrays
def mergeArrays(arr1, arr2):
  i = j = 0
  while i < len(arr1) and j < len(arr2):
    if arr2[j] <= arr1[i]:
      arr1.insert(i, arr2[j])
      j +=1
    else:
      if i == len(arr1)-1:
        arr1.append(arr2[j])
        j +=1
      i +=1
  return arr1

mergeArrays([1,2,3], [2,5,5])

# Product Defects
def largestArea(samples):
  if len(samples) == 0:
    return 0
  sizeOfArea =0
  # dynamic programming method: dp[len(sample)+1][len(sample[0])+1], all cells are 0
  dp = [[0 for i in range(len(samples)+1)] for j in range(len(samples[0])+1)]

  # dp[row][col] stores sizeOfArea
  for row in range(1, len(dp), 1):
    for col in range(1, len(dp[0]), 1):
      # if sample[row-1][col-1] == 1, dp[row][col] = min(dp[row-1][col-1], dp[row-1][col], dp[row][col-1])+1, meaning dp[row][col] increases 1 only if all surroundings are 1
      if samples[row-1][col-1] ==1:
        dp[row][col] = min(dp[row-1][col-1], dp[row-1][col], dp[row][col-1])+1
      # upadte sizeOfArea will be dp[row][col] or previous sizeOfArea whichever is larger
        sizeOfArea = max(sizeOfArea, dp[row][col])
  return sizeOfArea

largestArea([[1,1,1,1,1], [1,1,1,0,0], [1,1,1,0,0], [1,1,1,0,0], [1,1,1,1,1]])

# Perfect Team
import collections
def differentTeams(skills):
  if "p" not in skills or "c" not in skills or "m" not in skills  or "b" not in skills or "z" not in skills:
    return 0

  teamMap = collections.Counter(skills)
  return min(teamMap.values())
print(differentTeams("mppzbmbpzcbmpbmczczcccc"))
print(differentTeams("pcmpcmbbzz"))
print(differentTeams("pcmbp"))

# Next Permutation: return the next alphabetically greater string in all permutation of the word, if there is none of it, return "no answer"
def rearrangeWord(word):
  word = list(word) # conver string to char array
  for i in range(len(word)-1, 0, -1):
    for j in range(i-1, -1, -1):
      if word[i] > word[j]:
        word[i], word[j] = word[j], word[i]
        return "".join(word) # convert char array to string
  return "No answer"

print(rearrangeWord("pp"))
print(rearrangeWord("xy"))
print(rearrangeWord("hgfe"))
print(rearrangeWord("caba"))