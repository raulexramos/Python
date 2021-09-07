# Bot para clicar em videos do youtube

# Passo 1: Abrir o firefox
# Passo 2: Abrir o youtube
# Passo 3: Pesquisar Raulex Ramos
# Passs 4: Clicar no video
# Passo 5: Apertar like (apenas na primeira rodada)

import pyautogui as py
import time

#Abrir o youtube

py.click(397, 1048); #clica no crhome
time.sleep(5); #aguarda abrir

py.click(284, 84); #clica barra de endereço
time.sleep(2)#aguarda abrir
py.typewrite('youtube.com');#digita endereço
time.sleep(5) #aguarda digitar
py.press('return') #digita enter
time.sleep(3) #aguarda abrir

#Clica na barra de pesquisa e digita o nome
py.click(632, 130); #clica no campo de pesquisa do youtube
time.sleep(4)
py.typewrite('Raulex Ramos');
py.press('return')
time.sleep(4)


py.click(934, 262); #clica no nome rauelx
time.sleep(4)

py.click(412, 834); #clica no 01 video
time.sleep(10000) #tempo assistindo o video
py.click(20, 20); #volta para o canal
time.sleep(5) #tempo assistindo o video