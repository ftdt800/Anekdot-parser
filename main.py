import requests
from bs4 import BeautifulSoup
import pyautogui
import pyperclip
import keyboard

def get_text(url):
    rs = requests.get(url)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('td')

    return article.text


url = 'https://randstuff.ru/joke/'
while True:
    text = get_text(url)
# print(text)
    print(text[:100])  # Первые 100 символов из строки
    pyautogui.click(392, 1115)
    pyperclip.copy(text)
    keyboard.press_and_release('ctrl + v')
    pyautogui.press('enter')
