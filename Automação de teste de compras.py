
from gettext import install
from webbrowser import Chrome
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyautogui
import random

produtos = ('USB', 'Placa de video')
x = random.choice(produtos)




pyautogui.click(220,750,duration=2)
time.sleep(2)
pyautogui.write('Google Chrome')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(770,426,duration=2)
pyautogui.write('kabum')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=100, y=300)
time.sleep(3)
pyautogui.click(x=325, y=147)
pyautogui.write(x)
if x =='Placa de video':
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=390, y=560)
    time.sleep(3)
    pyautogui.click(x=1200, y=680)
    time.sleep(10)
    pyautogui.click(x=1250, y=143)
    time.sleep(10)
    pyautogui.press('PgDn')
    time.sleep(3)
    pyautogui.click(x=120, y=515)
    time.sleep(8)
    pyautogui.click(1122,567)
    time.sleep(3)
    pyautogui.click(224,560)
    time.sleep(3)
    pyautogui.press('PgDn')
    time.sleep(3)
    pyautogui.click(1094,447)
    time.sleep(3)
    pyautogui.press('pgdn')
    time.sleep(2)
    pyautogui.click(193,756)
    time.sleep(2)
    pyautogui.write('Email')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(213,54)
    time.sleep(2)
    pyautogui.write('Kabum')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(200,211)
    time.sleep(3)
    pyautogui.click(1021,394)
    pyautogui.click(1021,394)
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(3)
    pyautogui.click(24,106)
    time.sleep(2)
    pyautogui.write('eliassantos128@hotmail.com')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(529,230)
    time.sleep(3)
    pyautogui.write('Teste de compra')
    time.sleep(3)
    pyautogui.click(508,347)
    time.sleep(3)
    pyautogui.write('Esse é o número do pedido ')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.write(f'e o produto testado foi {x}')
    time.sleep(3)
    pyautogui.click(1281,57)
elif x =='USB':
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(480,632)
    time.sleep(3)
    pyautogui.click(1115,435)
    time.sleep(3)
    pyautogui.click(1267,155)
    time.sleep(3)
    pyautogui.press('PgDn')
    time.sleep(2)
    pyautogui.click(1176,579)
    time.sleep(3)
    pyautogui.click(288,548)
    time.sleep(3)
    pyautogui.press('PgDn')
    time.sleep(3)
    pyautogui.click(1049,444)
    time.sleep(3)
    pyautogui.press('pgdn')
    time.sleep(2)
    pyautogui.click(997,518)
    time.sleep(2)
    pyautogui.click(193,756)
    time.sleep(2)
    pyautogui.write('Email')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(213,54)
    time.sleep(2)
    pyautogui.write('Kabum')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(200,211)
    time.sleep(3)
    pyautogui.click(1021,394)
    pyautogui.click(1021,394)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(3)
    pyautogui.click(24,106)
    time.sleep(2)
    pyautogui.write('eliassantos128@hotmail.com')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(529,230)
    time.sleep(2)
    pyautogui.write('Teste de compra')
    time.sleep(3)
    pyautogui.click(508,347)
    time.sleep(3)
    pyautogui.write('Esse é o número do pedido ')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.write(f'e o produto testado foi {x}')
    time.sleep(3)
    pyautogui.click(1281,57)
    

    
    

   
    




    
  


    







    

   


    

  






































        
        




