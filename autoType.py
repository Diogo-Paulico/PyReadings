import webbrowser as wb, json, time
import pyautogui
import defineFunctions as fun


def start():
    fun.load()
    if not fun.anyPlace():
        noPlacesAddedMenu()
    else:
        menu()



def noPlacesAddedMenu():
    choice = input("""
                      A: Adicionar Local de Consumo
                      Q: Exit

                      Please enter your choice: """).lower()

    if choice =="a":
        register()
        menu()
    elif choice=="q":
        return
    else:
        print("You must selonlyect one of the available options")
        print("Please try again")
        noPlacesAddedMenu()



def menu():
    choice = input("""
                      A : Apagar Local de Consumo
                      E : Escolher Local de Consumo
                      L : Listar Locais de Consumo
                      Q : Exit

                      Please enter your choice: """).lower()

    if choice =="a":
        deletePlace()
        menu()
    elif choice=="e":
        placePicker()
        pickedMenu()
    elif choice=="l":
        placeDisplay()
        menu()
    elif choice=="q":
        exitS()
    else:
        print("You must select one of the available options")
        print("Please try again")
        menu()


def pickedMenu():
    choice = input("""
                      V : Ver Última Contagem
                      C : Comunicar Contagem
                      L : Voltar ao menu anterior
                      Q : Exit

                      Please enter your choice: """).lower()

    if choice =="v":
        showLastReading()
        pickedMenu()
    elif choice=="c":
        print("not yet")
        pickedMenu()
    elif choice=="l":
        menu()
    elif choice=="q":
        exitS()
    else:
        print("You must select one of the available options")
        print("Please try again")
        menu()


def placePicker():
    picked = 0
    counter = placeDisplay()
    print(list(range(1, counter)))
    while picked not in list(range(1, counter)):
        picked = int(input("Escolha um elemento da lista usando os seus numeros (1 - {0})".format(str(counter - 1))))
    placeName = fun.getAllPowerSpotsName()[picked-1]
    fun.choosePowerSpot(placeName)
    return picked
    


def placeDisplay():
    places = fun.getAllPowerSpotsName()
    counter = 1
    for placeName in places:
        print('{0}: {1} \n'.format(counter, placeName)) # will print the name as defined by the _str_ method
        counter += 1
    return counter

def register():
    name = input("Insira um nome único para o local de consumo: ")
    cpe = input("Insira o CPE (encontra-se na fatura e começa com PT): ")
    nif = nifEntry()
    typeOfMeter = int(typeEntry()) 
    choice = input("""
                    Deseja inserir uma leitura inicial? (Esta será adicionada ao sistema mas não comunicada) (SIM/NAO): 
                    """).strip().lower()
    fun.createNewPowerPlace(name, cpe, nif, typeOfMeter)
    if choice == "sim":
        fun.choosePowerSpot(name)
        addReading()
        fun.resetChoosenPlace()
        


def deletePlace():
    pick = placePicker()
    state = True if (input("Deseja apagar o local {0}? (SIM para confirmar, outro valor para anular)".format(pick)).strip().lower() == "sim") else False
    if state:
        fun.deletePowerSpot(pick)
        print("Apagado! \n")
    else:
        print("Anulado! \n")
    time.sleep(1)



def addReading():
    reading = []
    args = fun.getReadingArgs()
    for field in args:
        reading.append(input('{0}: '.format(field)))
    fun.updateReading(reading)


def showLastReading():
    reading = fun.getLastReading()
    print('Data: {0} \n'.format(reading.pop("date")))
    for x, y in reading.items():
        print('{0}: {1}').format(x,str(y)) 


def initialReadingEntry():
    choice = input("""
                    Deseja inserir uma leitura inicial? (SIM/NAO): 
                    """).strip().lower()
    if choice == "nao":
        return False
    elif choice == "sim":
        return True
    else:
        print("Por Favor insira SIM ou NAO \n")
        initialReadingEntry()



def typeEntry():
    meterSet = {"1","2","3"}
    typeOfMeter = input("""
                            1: Contador Simples
                            2: Contador bi-horário
                            3: Contador tri-horário
                            
                            Please enter your choice: """).strip()
    if typeOfMeter in meterSet:
        return typeOfMeter
    else:
        print("Deve inserir um tipo de contador válido (1, 2 ou 3)! \n")
        typeEntry()




def nifEntry():
    nif = input("Insira o NIF assiciado ao contrato: ").strip()
    if len(nif) != 9:
        print("O NIF deve conter 9 dígitos! \n")
        return nifEntry()
    else:
        return nif

    

def exitS():
    fun.save()
    return

""" 

wb.open('https://www.e-redes.pt/pt-pt/podemos-ajudar/comunicar-leituras', new=1, autoraise=True)


def altTab():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')


#input()        
# altTab()
pyautogui.confirm('Is the browser window in focus?', buttons=['Yes', 'No'])

# pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])

pyautogui.write('PT0002000081906841LA')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('197102670')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
 """





start()
