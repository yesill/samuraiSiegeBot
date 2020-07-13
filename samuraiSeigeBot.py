#28/02/2020 - updated: 01/03/2020
# author: yesill 
# com: yslmehmetbm@gmail.com

import pyscreenshot as pyss
from PIL import Image   #masaustu cozunurlugunu dikkate almayi unutma!!!!
from pynput.mouse import Button, Controller as mCtrl
from pynput.keyboard import Key, Controller as kCtrl
import datetime
import random
import time
import sys
import os

mouse = mCtrl()
keyBoard = kCtrl()
yesil = ((7,148,0),(15,156,8))  #yesil rgb araligi
kirliBeyaz = ((234,234,212),(244,244,222))
kapiColorBorders = ((58,50,37),(68,60,47))
battleButtonColorBorders = ((210,100,0),(234,129,13))
SaldirilabilirSayaci = 0
SaldirilamazSayaci = 0

def fSaldiriRatio():
    if SaldirilabilirSayaci == 0 and SaldirilamazSayaci == 0:   return "0 %"
    return str((float(SaldirilabilirSayaci) / (float(SaldirilabilirSayaci) + float(SaldirilamazSayaci))) * 100) + " %"

def fSayacPrint():  #sadece sayac, +1 ler yok..!
    os.system('cls')
    print("Saldirildi: " + str(SaldirilabilirSayaci) + "   Saldirilamadi: " + str(SaldirilamazSayaci) + "   Saldiri orani: " + fSaldiriRatio())

def fSayacPrintp1m1(saldiriBool):   #True -> saldirilabilir, False -> saldirilamaz
    os.system('cls')
    print("Saldirildi: " + str(SaldirilabilirSayaci) + "   Saldirilamadi: " + str(SaldirilamazSayaci) + "   Saldiri orani: " + fSaldiriRatio())
    if saldiriBool:
        print("Saldirilabilir hedef +1")
    else:
        print("Saldirilamaz hedef +1")

def fGetSS(x,y):
    img = pyss.grab().load()
    return img[x,y]

def fCheckBandage(liste):   #liste[0] = r , liste[1] = g , liste[2] = b

    bandage = False
    tb = ((230, 230, 230), (235, 193, 0), (210, 100, 0))    #taban
    tv = ((250, 250, 250), (255, 213, 10), (250, 130, 20))   #tavan
    
    #liste[0] = r , liste[1] = g , liste[2] = b
    
    if (liste[1] >= tb[0][1] and liste[1] <= tv[0][1]):   # item 0 g
        if (liste[0] >= tb[0][0] and liste[0] <= tv[0][0]) and (liste[2] >= tb[0][2] and liste[2] <= tv[0][2]):
            bandage = True
        else:
            bandage = False

    elif (liste[1] >= tb[1][1] and liste[1] <= tv[1][1]): # item 1 g
        if (liste[0] >= tb[1][0] and liste[0] <= tv[1][0]) and (liste[2] >= tb[1][2] and liste[2] <= tv[1][2]):
            bandage = True
        else:
            bandage = False

    elif (liste[1] >= tb[2][1] and liste[1] <= tv[2][1]): # item 2 g
        if (liste[0] >= tb[2][0] and liste[0] <= tv[2][0]) and (liste[2] >= tb[2][2] and liste[2] <= tv[2][2]):
            bandage = True
        else:
            bandage = False

    else:
        bandage = False

    return bandage

def fClick(x,y):
    pos = (x,y)
    while True:
        if mouse.position == (pos):
            mouse.click(Button.left,1)
            break
        else:
            mouse.position = pos

def fKey(key):
    keyBoard.press(key=key)
    keyBoard.release(key=key)

def fAttack():
    unit = 0

    for i in range(0,2):
        #troop select
        if unit == 0:   #rashoumon
            fClick(244,762) #rashoumon
            unit = 1
        elif unit == 1: #bonus troops
            fClick(775,770) #bonus troops
            unit = 0

        #troop deploy
        delay = 0.2
        positions = ((644,541),(284,396),(1166,262),(1187,750),(1022,674),(135,689),(20,265))
        tekrarsizList = list()
        while True:
            randomSayi = random.randint(0,6)
            i = positions[randomSayi]
            if i not in tekrarsizList:
                tekrarsizList.append(i)
                if len(tekrarsizList) == 7:
                    break
            else:   continue

        def fAttackClick(demet):
            time.sleep(delay)
            fClick(demet[0],demet[1])
        
        for pos in tekrarsizList:
            fAttackClick(pos)

def fKapiCheck():
    failSafeSayac = 0
    while True: #kapi acilana kadar
        time.sleep(0.5)
        tempList = fGetSS(750,250)
        if ((tempList <= kapiColorBorders[0]) or (tempList >= kapiColorBorders[1])):
            print("kapilar acildi..!")
            time.sleep(0.5)   #ss alınmadan önce bekliyor ki kapi bandage in ustunu kapatmasin
            break

def fHomeTown():

    def fHomeTownControl():

        def fRetreat():
            while True:
                L0 = fGetSS(746,866)
                L1 = fGetSS(766,866)
                L2 = fGetSS(786,866)
                if (((L0 >= yesil[0]) and (L0 <= yesil[1])) and ((L1 >= kirliBeyaz[0]) and (L1 <= kirliBeyaz[1])) and ((L2 >= yesil[0]) and (L2 <= yesil[1]))):
                    fClick(460,690) #left button = yes
                    fBackHome()
                    break
                else:
                    break

        while True:
            breakBool = False
            os.system('cls')
            print("home town control")
            tempList = fGetSS(1454,996)
            if ((tempList >= battleButtonColorBorders[0]) and (tempList <= battleButtonColorBorders[1])):
                os.system('cls')
                print("Battle..!")
                fClick(1163,775)    #battle button
                break
            else:
                if (fGetSS(770,186) != (167,23,23)):
                    fClick(610,200)     #return the village or retreat clicked
                    print("Return - Retreat")
                    time.sleep(1)
                    fRetreat()  #retreat
                    fKapiCheck()
                else:   #errorLog
                    with open('errorLog.txt', 'w+') as file:
                        file.write("homeTownControl error='3'")

    def fBattleButtonGreenClick():
        while True:
            tempList = fGetSS(760,1020)
            if ((tempList >= yesil[0]) and (tempList <= yesil[1])):
                fClick(614,805) #2700 battle
                break
    
    fHomeTownControl()
    time.sleep(1)
    fBattleButtonGreenClick()
    time.sleep(0.7)
    fClick(472,677) #shield continue

def fPlayTime():
    while True:
        L0 = fGetSS(746,866)
        L1 = fGetSS(766,866)
        L2 = fGetSS(786,866)
        if (((L0 >= yesil[0]) and (L0 <= yesil[1])) and ((L1 >= kirliBeyaz[0]) and (L1 <= kirliBeyaz[1])) and ((L2 >= yesil[0]) and (L2 <= yesil[1]))):
            fClick(760,690) #right button = yes
            break
        else:
            break

def fBackHome():
    while True:     #home town donme
        time.sleep(1)
        tempList = fGetSS(640,880)
        if ((tempList >= yesil[0]) and (tempList <= yesil[1])):   #continue butonun oldugu yer yesil ise
            fClick(509,694) #continue button
            break

def fStartPrompt():
    os.system('cls')
    startTime = random.randint(3,7)
    print(str(startTime + 1) + "sn bekleyin..!")
    time.sleep(startTime)
    os.system('cls')

#start
while True: #main loop
    fStartPrompt()
    fPlayTime()
    fHomeTown()
    fSayacPrint()
    while True:     #battle loop
        fKapiCheck()
        if fCheckBandage(fGetSS(53,213)):   #SSbandage
            SaldirilabilirSayaci += 1
            fSayacPrintp1m1(True)    #True -> saldirilabilir, False -> saldirilamaz
            fAttack()
            fBackHome()
            break
        else:
            SaldirilamazSayaci += 1
            fSayacPrintp1m1(False)    #True -> saldirilabilir, False -> saldirilamaz
            fClick(611,657)     #next button
#end