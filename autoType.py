import webbrowser as wb
from time import sleep
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
        print("You must select one of the available options")
        print("Please try again")
        sleep(3)
        clear()
        noPlacesAddedMenu()



def menu():
    choice = input("""
            A : Adicionar Local de Consumo
            R : Apagar Local de Consumo
            E : Escolher Local de Consumo
            L : Listar Locais de Consumo
            Q : Exit

            Please enter your choice: """).lower()

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
    elif choice=="q":
        exitS()
    else:
        print("You must select one of the available options")
        print("Please try again")
        sleep(3)
        clear()
        menu()


def pickedMenu():
    #clear()
    choice = input("""
                      V : Ver Última Contagem
                      C : Comunicar Contagem
                      L : Voltar ao menu anterior
                      Q : Exit

                      Please enter your choice: """).lower()
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
    elif choice=="q":
        exitS()
    else:
        print("You must select one of the available options")
        print("Please try again")
        sleep(3)
        clear()
        menu()


def chooseCurrentPlace():
    name = placePicker()
    fun.choosePowerSpot(name)


def placePicker():
    picked = 0
    counter = placeDisplay()
    while picked not in list(range(1, counter)):
        picked = int(input("Escolha um elemento da lista usando os seus numeros (1 - {0}): ".format(str(counter - 1))))
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
    cpe = input("Insira o CPE (encontra-se na fatura e começa com PT): ")
    nif = nifEntry()
    typeOfMeter = int(typeEntry()) 
    choice = input("""
                    Deseja inserir uma leitura inicial? (Esta será adicionada ao sistema mas não comunicada) (SIM/NAO):  """).strip().lower()
    fun.createNewPowerPlace(name, cpe, nif, typeOfMeter)
    if choice == "sim":
        fun.choosePowerSpot(name)
        addReading(False)
        fun.resetChoosenPlace()
    clear()
        


def deletePlace():
    pick = placePicker()
    state = True if (input("Deseja apagar o local {0}? (SIM para confirmar, outro valor para anular)".format(pick)).strip().lower() == "sim") else False
    if state:
        fun.deletePowerSpot(pick)
        print("Apagado! \n")
    else:
        print("Anulado! \n")
    sleep(1)



def addReading(communicate):
    reading = []
    args = fun.getReadingArgs()
    for field in args:
        reading.append(int(input('{0}: '.format(field))))
    result = fun.updateReading(*reading)
    if not result:
        print('A contagem é inferior à registada anteriormente. Tente novamente! \n')
        return

    if communicate:
        communicateReading(reading)


def communicateReading(reading):
    wb.open('https://www.e-redes.pt/pt-pt/podemos-ajudar/comunicar-leituras', new=1, autoraise=True)
    input("""
        Coloque a janela do browser em foco (Pressione uma zona cinzenta por cima do campo CPE) 
        e depois volte a esta janela e pressione Enter!, quando aparecer os campos para 
        colocar a contagem volte aqui""")        
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
    input('Pressione Enter para escrever a contagem! Confirme o valor e pressione "Submeter Leitura"')
    sleep(0.2)
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


def nameEntry():
    choice = input("Insira um nome único para o local de consumo: ").strip()
    if fun.checkIfPlaceDoesNotExist(choice):
        return choice
    else:
        print("Por Favor insira um nome não repetido")
        nameEntry()

def initialReadingEntry():
    choice = input("""
    Deseja inserir uma leitura inicial? (SIM/NAO): """).strip().lower()
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
    sleep(.2)
    press('tab')
    sleep(.2)
    keyUp('alt')
    sleep(.2)

""" 


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

