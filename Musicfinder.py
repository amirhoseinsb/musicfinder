# import library
from bs4 import BeautifulSoup
import requests


def banner():
    print("""
            
 __  __           _        _____ _           _           
|  \/  |_   _ ___(_) ___  |  ___(_)_ __   __| | ___ _ __ 
| |\/| | | | / __| |/ __| | |_  | | '_ \ / _` |/ _ \ '__|
| |  | | |_| \__ \ | (__  |  _| | | | | | (_| |  __/ |   
|_|  |_|\__,_|___/_|\___| |_|   |_|_| |_|\__,_|\___|_|   
                                                         
Created By : AmirhoseinSohrabi
Gmail : amirhoseinsohrabi.official@gmail.com            
            
            """)

def input_name():# input the name
    global name
    name = input("Enter The Singer Name : ")
    
    
def requests_():# send request to google
    global req
    session = requests.session()
    session.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36'})
    req = session.get(f"https://www.google.com/search?q=intitle%3Aindex+of+mp3+intext%3A%22{name}%22")
    
    
def filter_():# Filter the Content
    global link
    soup = BeautifulSoup(req.content,'html.parser')
    link = soup.select('a')

    
def find():#Find the Link
    global z
    z = []
    for i in link :
       x = (i.get('href'))
       z.append(x)


def view():# VIew the Link
    number = 0
    link = z[9:19]
    for finder in link :
        number += 1
        print(f'Link : {number} {finder}\n')
