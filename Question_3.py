Animal = []
Colour = []
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush):
    if AnimalTopPointer == 20:
       return False
    else:
        Animal.append(DataToPush)
        AnimalTopPointer +=1
        return True
    
def popAnimal():
    # global AnimalTopPointer
    # global ColourTopPointer
    if AnimalTopPointer == 0:
        return ''
    else:
        ReturnData = Animal[AnimalTopPointer - 1] 
        AnimalTopPointer -=1 
        return ReturnData

def ReadData(): 
 try: 
    global AnimalTopPointer 
    global ColourTopPointer 
    AnimalFile = open("AnimalData.txt", 'r') 
    for Line in AnimalFile: 
        PushAnimal(Line) 
        AnimalFile.close() 
 except IOError: 
    print("Could not find file")

def PushColour(DataToPush):
    if ColourTopPointer == 20:
        False
    else:
        Colour.append(DataToPush)
        ColourTopPointer +=1
        return True

def popColour():
    global AnimalTopPointer
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ''
    else:
        ReturnData = Colour[ColourTopPointer - 1] 
        ColourTopPointer -=1 
        return ReturnData
def ReadData(): 
 try: 
    ColourFile = open("Colour.txt", 'r') 
    for Line in ColourFile: 
        PushColour(Line) 
        ColourFile.close() 
 except IOError: 
    print("Could not find file")   

def OutputItem(): 
 global AnimalTopPointer 
 global ColourTopPointer 
 ColourReturned = popColour() 
 AnimalReturned = popAnimal() 
 if ColourReturned == "": 
    print("No colour") 
    PushAnimal(AnimalReturned) 
 else: 
    if AnimalReturned == "": 
        print("No animal") 
        PushColour(ColourReturned) 
    else: 
        print(ColourReturned, AnimalReturned)

ReadData() 
OutputItem()