import pyautogui as ptg
import pyperclip
from time import sleep

# Abrir o Chrome/Abrir FY
ptg.hotkey('win','r')
sleep(0.5)
ptg.typewrite('chrome')
ptg.press('enter')
sleep(1)
ptg.click(x=962, y=602)
sleep(1)

ptg.typewrite('https://docs.google.com/spreadsheets/d/1biIcNT7i-dOFssfD0aXFmrsUO00lhnk6H64SweExbIc/edit#gid=1673114418')
ptg.press('enter')
sleep(10)

# Fazer procedimento diário
ptg.hotkey('ctrl','down')
sleep(5)
ptg.hotkey('ctrl','down')
sleep(5)

# Copiar células
ptg.keyDown('ctrl')
sleep(0.2)
ptg.press('c')
sleep(0.3)
ptg.keyUp('ctrl')
sleep(0.5)

for i in range(12):
    ptg.press('down')
    ptg.hotkey('ctrl','v')
    sleep(0.1)

for i in range(5):
    ptg.press('up')

#COLETAR CONSOLID
for i in range(7):
    ptg.press('right')

ptg.hotkey('ctrl','c')
sleep(0.5)
consolid = pyperclip.paste()

ptg.press('down')
ptg.press('down')
sleep(0.5)

ptg.hotkey('ctrl','c')
sleep(0.5)
masipack = pyperclip.paste()
ptg.press('down')

ptg.hotkey('ctrl','c')
sleep(0.5)
envase1 = pyperclip.paste()
ptg.press('down')

ptg.hotkey('ctrl','c')
sleep(0.5)
envase2 = pyperclip.paste()
ptg.press('down')
sleep(0.5)

#Mandar a mensagem via Slack
ptg.hotkey('win','r')
sleep(0.5)
ptg.typewrite('notepad')
ptg.press('enter')
sleep(1)

ptg.typewrite('Totais pre-reuniao diaria [17h30]')
ptg.press('enter')
ptg.typewrite('=======================================================')
ptg.press('enter')
ptg.press('enter')
ptg.typewrite(f'* Consolid: 	{consolid}')
ptg.press('enter')
ptg.press('enter')
ptg.press('enter')
ptg.press('enter')

ptg.typewrite(f'* Masipack: 	{masipack}')
ptg.press('enter')

ptg.typewrite(f'* Envase 1: 	{envase1}')
ptg.press('enter')

ptg.typewrite(f'* Envase 2: 	{envase2}')
ptg.press('enter')