from bs4 import BeautifulSoup
from PIL import I
import requests,os
# I Have Used A Class So That More Methods Can Be Added In Future.
class Downloader():
    def __init__(self,folder,url):
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
        self.code=requests.get(url,headers=self.headers).content
        self.soup=BeautifulSoup(self.code,'html.parser')
        self.imlinks=[]
    def create(self):
        try:
            os.mkdir(folder)
        except FileExistsError:
            print('Folder Already exists Give A Unique Name.')
    def scrape(self):
        self.create()
        self.imlinks=self.soup.find_all('img')
    def download(self):
        self.scrape()
        print(f"Images Total:-{len(self.imlinks)}")
        for j,i in enumerate(self.imlinks,1):
            link=requests.get(i['src']).content
            with open(f'{folder}/Img{j}.jpg','wb+') as f:
                f.write(link)
url=input('Paste the url Here -> ')
folder=input('Enter the Folder name you want to store the images in ')
imgs=Downloader(folder,url)
imgs.download()