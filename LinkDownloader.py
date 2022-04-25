import requests
from bs4 import BeautifulSoup
import os

def banner():
    print('''
 _     _       _    ____                      _                 _           
| |   (_)_ __ | | _|  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __ 
| |   | | '_ \| |/ / | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
| |___| | | | |   <| |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
|_____|_|_| |_|_|\_\____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                                         
Created By : amirhoseinsohrabi
Gmail : amirhoseinsohrabi.official@gmail.com                                                                        

    ''')
def url():#input url
    global url
    url = input('Enter The link : \n')

def requests_():# send the request
    global req
    session = requests.session()
    session.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36'})
    req = session.get(url)
    
    
def linkfinder():# find the download link
    global link
    soup = BeautifulSoup(req.content,'html.parser')
    link = soup.select('a+ a')
    
    
def output():# export the link
    global downloadlink
    downloadlink = []
    print("____________________________________________________________________\n")
    number = 0
    for i in link:
         number += 1
         x = (i.get('href'))
         print(f'Download Link {number} : {url}{x}\n')
         downloadlink.append(f'{url}{x}') 
         
         
def downloadlinkfile():# create the text file for download the music with download manager
    file_name = "Downloadlink.txt"
    try:
        os.remove('Downloadlink.txt')
    except:
        print('Downloadlink.txt File is Created !')
    
    for i in downloadlink:
        file = open(file_name, "a+")
        file.write(f'{i}\n')
        file.close()
 
banner()
url()
requests_()
linkfinder()
output()
downloadlinkfile()