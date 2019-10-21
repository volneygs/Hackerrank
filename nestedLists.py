def nestedLists(num, names, grades):

    lowest = grades[0]
    secondLowest = grades[0]

    lowestList = []

    for i in range(len(names)):
        if(grades[i] < lowest):
            lowest = grades[i]

    for j in range(len(names)):
        if(grades[j] != lowest):
            secondLowest = grades[j]
        
    for k in range(len(names)):
        if(grades[k] <= secondLowest and grades[k] > lowest):
            secondLowest = grades[k]

    for p in range(len(names)):
        if(grades[p] == secondLowest):
            lowestList.append(names[p])


    return lowestList

num = int(input())

names = []
grades = []

for i in range(num):
    
    names.append(input())
    grades.append(float(input()))


lowestList = nestedLists(num, names, grades)

sortedLowestList = sorted(lowestList)

for h in range(len(sortedLowestList)):
    print(sortedLowestList[h])