"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Michal Bouška
email: michal.bouska93@gmail.com
"""

import random
import time

number = list()
attempts = 0

def CreateNumber():
    '''Generuje náhodné čtyřciferné číslo, které nezačíná nulou'''
    for _ in range(4):
        x = random.randrange(0,9)
        number.append(x) 
    if len(number) > len(set(number)) or int(number[0]) == 0:
        number.clear()
        CreateNumber()

def Game():
    '''Kontroluje vstup uživatele a následně ho porovnává s náhodným číslem z CreateNumber()'''
    global attempts
    attempts += 1
    cows = 0
    bulls = 0
    #print(number)
    is_the_user_input_ok = False
    while is_the_user_input_ok is False:
        choice = input('Tvůj tip: ')
        if not choice.isdigit():
            print('Zadejte číslo!!!')
            print('='*50) 
            is_the_user_input_ok = False
        elif int(len(choice)) != 4:
            print('Zadané číslo musí být čtyřciferné!!!')
            print('='*50) 
            is_the_user_input_ok = False
        elif int(choice[0]) == 0:
            print('Zadané číslo nesmí začínat nulou!!!')
            print('='*50)
            is_the_user_input_ok = False
        elif len(choice) > len(set(choice)):
            print('Zadané číslo musí být unikátní!!!')
            print('='*50)
            is_the_user_input_ok = False
        else:
            is_the_user_input_ok = True
    else:
        user_number = list()
        for i in range(4): 
            user_number.append(int(choice[i])) #přidání zadaného čísla do listu, který se bude procházet  
            
    for x in range(4): 
        for y in range(4): 
            if (user_number[x] == number[y]): #kontrola cows - stejné číslo na rozdílných pozicích
                cows += 1             
    for x in range(4):
        if user_number[x] == number[x]: #kontrola bulls - stejné číslo na stejném místě v listu
            bulls += 1  
                        
    print('Bulls: ', bulls)
    print('Cows: ', cows)
    print('='*50)
        
    if bulls == 4:
        num = ''
        for i in number:
            num += str(i) 
        print(f'Vyhráli jste!\nTajné číslo je {num}, zvládli jste to na {attempts} pokus.')
        print('='*50)     
    else:
        Game()

if __name__ == "__main__":   
    while True:
        print('='*50)
        print('Pojďme si zahrát hru "Bulls and cows"!')
        time.sleep(1)          
        print('Myslím si unikátní čtyřciferné číslo, které nezačíná nulou.\nJaké to je?')
        CreateNumber()
        print('='*50)
        start_time = time.time()
        Game()
        end_time = time.time()
        total_time = int(round(end_time-start_time,0))
        if total_time < 60:
            print(f'Zjistit tajné číslo ti trvalo {total_time:.1f} sekund. To bylo fakt rychlé!!!')
        else:
            print(f'Zjistit tajné číslo ti trvalo {total_time:.1f} sekund. To tedy nic moc....Nechceš to zkusit znovu a lépe?')
        
        time.sleep(2)
        continue_game = input('Přeješ si pokračovat ve hře?\nNapiš A pro ano, nebo jakýkoliv jiný znak pro ne:')
        
        if continue_game == 'A':
            print('='*50)
            True       
        else:
            print('Program se ukončuje...')
            print('='*50)
            break
        
        
        


        
    
