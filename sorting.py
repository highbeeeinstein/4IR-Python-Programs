ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
n = len(ages) - 1
for i in range(len(ages) - 1):
    for j in range(n):
        if ages[j] > ages[j+1]:
            Temp = ages[j]
            ages[j] = ages[j+1]  
            ages[j+1] = Temp
    n= n-1
# print(ages)
max_age = ages[-1]
min_age = ages[0]
ages.append(max_age)
ages.append(min_age)

print(ages)

def Median(sortedlist):
    n = len(sorted(sortedlist))
    if n % 2 == 0 :
        median = (sortedlist[n//2 - 1] + sortedlist[n//2])/2 
    else:
        median = sortedlist[n//2]
    return median
print(Median(ages))