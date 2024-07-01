DataArray = []
DataFile = open("Data.txt",'r')
for line in DataFile:
    DataArray.append(int(line))

def PrintArray(DataArray): 
 output = "" 
 for X in range(0, len(DataArray)): 
    output +=  str((DataArray[X])) + " " 
 print(output)

PrintArray(DataArray)

def LinearSearch(DataArray, DatatoFind):
   Count = 0
   for X in range(0, len(DataArray)):
     if (DataArray[X] == DatatoFind):
      Count +=1
   return Count
# LinearSearch(DataArray, 7)
DataToFind = int(input("Enter a number to find ")) 
while DataToFind < 0 or DataToFind > 100: 
    DataToFind = int(input("Enter a number to find ")) 
NumberTimes = LinearSearch(DataArray, DataToFind) 
print("The number", DataToFind, "is found", NumberTimes, "times")

