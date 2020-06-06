import pyautogui as p
import time, webbrowser, pyperclip
import requests
import re
from bs4 import BeautifulSoup
import wikipedia as wk
from urllib.request import urlopen
def msgPlace():
    p.click(691,729)
def cpyRply():
    p.click(613,669)
    time.sleep(1)
    p.dragTo(925,675)
    p.hotkey('ctrl','c')
    return pyperclip.paste()
def findNew():
    color = p.pixel(496,381) #green color of new message
    if color[0] == 6 and color[1] == 215:
        print("New message Found")
        p.click(480,381)
name = input("Enter the name of (user")
webbrowser.open('https://web.whatsapp.com')
time.sleep(40)
p.click(308,245)
time.sleep(1)
p.typewrite(name + "\n")
time.sleep(1)
msgPlace()
time.sleep(10)
reply = cpyRply()
while True:
    print(reply)
    reply = cpyRply()
    if ("hi" or "hello") in reply:
        p.typewrite("Hello\nHow are you?\n")
    if ("fine" or "mast" or "thik hu") in reply:
        p.typewrite("kya ho rha h?\n")
    if ("kuch nhi" or "nothing") in reply:
        p.typewrite("to kuch kro\nKoi kaam nhi hai kya?\n")
    if ("your name") in reply:
        p.typewrite("My name is PBot.\nand i think your name is " + name + "\n")
    if ("nice" or "good") in reply:
        p.typewrite("Really!!??")
    if ("yes") in reply:
        p.typewrite("Ohhh!!")
    if ("fav color" or "favourite color") in reply:
        p.typewrite("Favourite is Red.(May be hehehe)\n")
    if ("bye") in reply:
        p.typewrite("Bye Nice to talk your\nTalk you later.\n")
    if ("food" or "dish" or "like to eat") in reply:
        p.typewrite("I like to use Electricty Hehehe\n")
    if ("news") in reply:
        p.typewrite("Please Wait i am trying to get some latest news from google news\n")
        news_url = "https://news.google.com/news/rss"
        Client = urlopen(news_url)
        xml_page = Client.read()
        Client.close()
        soup_page = BeautifulSoup(xml_page,"html.parser")
        news_list = soup_page.findAll("item")
        print("News are")
        for news in news_list[:10]:
            p.typewrite(news.title.text+"\n")
    if ("tell me about") in reply:
        topic = re.search("tell me about (.+)",reply).group(1)
        summary = wk.summary(topic)
        p.typewrite(summary)
    if ("how are you") in reply:
        p.typewrite("I am fine\n Thanks for care\n")
    if ("your age") in reply:
        p.typewrite("I was created onHeHow are you?Dec 22 2019.\nNow i think you can calculate my age\n")
    if ("you like") in reply:
        p.typewrite("Well certainly, I like eveything\n")
    if ("your owner") in reply:
        p.typewrite("You can call him Prince Vishwakarma\n")
    if ("sorry") in reply:
        p.typewrite("Oh! Never mind.\n")
    if ("what are you doing") in reply:
        p.typewrite("Chatting with "+name+"\n")
    time.sleep(5)
