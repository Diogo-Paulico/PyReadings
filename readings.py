import webbrowser as wb
import time
from pyautogui import press, write as typeT, keyDown, keyUp
import defineFunctions as fun
from os import system, name


def start():
    clear()
    fun.load()
    if not fun.anyPlace():
        noPlacesAddedMenu()
    else:
        menu()



def noPlacesAddedMenu():
    choice = input(fun.getString("noplacesmenu") + fun.getString("enterchoice")).lower() #lang["en"]["noplacesmenu"] + lang["en"]["enterchoice"]

    if choice =="a":
        register()
        menu()
    elif choice == "t":
        clear()
        fun.toggleLanguage()
        noPlacesAddedMenu()
    elif choice=="q":
        return
    else:
        print(fun.getString("selectavailable"))
        print(fun.getString("tryagain"))
        time.sleep(3)
        clear()
        noPlacesAddedMenu()



def menu():
    choice = input(fun.getString("menu") + fun.getString("enterchoice")).lower()

    clear()
    if choice =="r":
        deletePlace()
        menu()
    elif choice == 'a':
        register()
        menu()
    elif choice=="e":
        chooseCurrentPlace()
        clear()
        pickedMenu()
    elif choice=="l":
        placeDisplay()
        menu()
    elif choice == "t":
        clear()
        fun.toggleLanguage()
        menu()
    elif choice=="q":
        exitS()
    else:
        print(fun.getString("selectavailable"))
        print(fun.getString("tryagain"))
        time.sleep(3)
        clear()
        menu()


def pickedMenu():
    #clear()
    choice = input(fun.getString("pickedmenu") + fun.getString("enterchoice")).lower()
    clear()
    if choice =="v":
        showLastReading()
        pickedMenu()
    elif choice=="c":
        addReading(True)
        pickedMenu()
    elif choice=="l":
        fun.resetChoosenPlace()
        menu()
    elif choice == "t":
        clear()
        fun.toggleLanguage()
        pickedMenu()
    elif choice=="q":
        exitS()
    else:
        print(fun.getString("selectavailable"))
        print(fun.getString("tryagain"))
        time.sleep(3)
        clear()
        pickedMenu()


def chooseCurrentPlace():
    name = placePicker()
    fun.choosePowerSpot(name)


def placePicker():
    picked = 0
    counter = placeDisplay()
    while picked not in list(range(1, counter)):
        picked = int(input(fun.getString("placepicker").format(str(counter - 1)))) #placepicker
    placeName = fun.getAllPowerSpotsName()[picked-1]
    return placeName
    


def placeDisplay():
    places = fun.getAllPowerSpotsName()
    counter = 1
    for placeName in places:
        print('{0}: {1} \n'.format(counter, placeName)) # will print the name as defined by the _str_ method
        counter += 1
    return counter

def register():
    clear()
    name = nameEntry()
    cpe = input(fun.getString("cpeinput")) #cpeinput
    clear()
    nif = nifEntry()
    typeOfMeter = int(typeEntry()) 
    fun.createNewPowerPlace(name, cpe, nif, typeOfMeter)
    if initialReadingEntry():
        fun.choosePowerSpot(name)
        addReading(False)
        fun.resetChoosenPlace()
    clear()
        


def deletePlace():
    pick = placePicker()
    state = True if (input(fun.getString("deleteconfirm").format(pick)).strip().lower() == fun.getString("acceptword") ) else False #acceptword and deleteconfirm
    if state:
        fun.deletePowerSpot(pick)
        print(fun.getString("deleted")) #deleted
    else:
        print(fun.getString("canceled")) #canceled
    time.sleep(1)



def addReading(communicate):
    reading = []
    args = fun.getReadingArgs()
    for field in args:
        reading.append(int(input('{0}: '.format(field))))
    result = fun.updateReading(*reading)
    if not result:
        print(fun.getString("lowreading")) #lowreading
        return

    if communicate:
        communicateReading(reading)


def communicateReading(reading):
    wb.open('https://www.e-redes.pt/pt-pt/podemos-ajudar/comunicar-leituras', new=1, autoraise=True)
    input(fun.getString("browser1"))     #browser1    
    altTab()
    press('tab')
    typeT(fun.getChoosenPlaceCPE())
    press('tab')
    press('tab')
    typeT(fun.getChoosenPlaceNIF())
    press('tab')
    press('tab')
    press('tab')
    press('enter')
    clear()
    input(fun.getString("submitreading"))
    time.sleep(0.2)
    altTab()
    press('tab')
    typeT(str(reading[0]))
    fields = len(reading) - 1
    if fields == 0:
        for x in range(0, fields):
            press('tab')
            typeT(str(reading[x+1]))
    press('tab')
    press('tab')




def showLastReading():
    reading = fun.getLastReading()
    print('Data: {0} \n'.format(reading.pop("data")))
    for x, y in reading.items():
        print('{0}: {1}'.format(x,str(y)))
    print("\n")


def nameEntry():
    choice = input(fun.getString("placename")).strip() #placename
    if fun.checkIfPlaceDoesNotExist(choice):
        return choice
    else:
        print(fun.getString("uniquenamewarning")) #uniquenamewarning
        nameEntry()

def initialReadingEntry():
    choice = input(fun.getString("firstreadingquery")).strip().lower() #firstreadingquery
    if choice == fun.getString("cancelword"): #cancelword
        return False
    elif choice == fun.getString("acceptword"): #acceptword
        return True
    else:
        print(fun.getString("pleaseyn")) #pleaseyn
        initialReadingEntry()



def typeEntry():
    meterSet = {"1","2","3"}
    typeOfMeter = input(fun.getString("metertype") + fun.getString("enterchoice")).strip() #metertype and selectavailable
    if typeOfMeter in meterSet:
        return typeOfMeter
    else:
        print(fun.getString("validmeter")) #validmeter
        typeEntry()




def nifEntry():
    nif = input(fun.getString("nifinput")).strip() #nifinput
    if len(nif) != 9:
        print(fun.getString("nif9digits")) #nif9digits
        return nifEntry()
    else:
        return nif

    

def exitS():
    fun.save()
    clear()
    return


def clear():
        if name == "nt":

        #if windows, linux
            _ = system("cls")

        else:
        #mac, etc.
            _ = system("clear")


def altTab():
    keyDown('alt')
    time.sleep(.2)
    press('tab')
    time.sleep(.2)
    keyUp('alt')
    time.sleep(.2)


start()