from random import randint as rnd
import random
import pandas as pd
import string



def nome_aleatorio(tamanho, quantidade):
    vogal = 'aeiouAEIOU' 
    consoante = ''.join([x for x in string.ascii_letters if x not in vogal])
    nome = []
    nomes = []
    for q in range(quantidade):
        optL = [vogal, consoante]
        rndop = rnd(0,1)
        nome = []
        for i in range(tamanho):
            l1 = random
            if i % 2 == 0:
                nome.append(random.choice(optL[rndop]))
            else:
                nome.append(random.choice(optL[rndop-1]))
        nomes.append(''.join(nome).capitalize())
    return nomes

def addFile(fileName, linesN):    
    for line in range(linesN):
        name = nome_aleatorio(rnd(4,10),rnd(2,4))
        date = str(rnd(2000,2024)) + '/' + str(rnd(1,12)).zfill(2) + '/' + str(rnd(1,30)).zfill(2)
        regN = rnd(10000,99999)
        options = ['YES','NO']
        option = options[rnd(0,1)]
        with open(fileName,'a+') as file:
            file.seek(0)
            qtdLines = str(len(file.readlines()) +1).zfill(3)
            file.write(f'Name: {' '.join(name)}\tQtd: {qtdLines}\tRN: {regN}\tDate: {date}\tAvailable: {option}\n')
            
fileName = 'memberList3.txt'

addFile(fileName,5)

with open(fileName,'r') as openFile:
    print(openFile.read())
