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
