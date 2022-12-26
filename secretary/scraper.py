from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests
 
 
# 抽象類別
class Stock(ABC):
 
    def __init__(self, num):
        self.num = num  # stock number
 
    @abstractmethod
    def scrape(self):
        pass
 
 
# 爬蟲
class Gate(Stock):
 
    def scrape(self):
        response = requests.get(
            "https://humandesign.tools/hd-gates/gate-" + self.num )
 
        soup = BeautifulSoup(response.content, "html.parser")
 
        # 爬取卡片資料
        cards = soup.find_all(
            'div', {'class': 'app_pageContent__PSDsN'}, limit=1)
 
        content = ""
        for card in cards:
           pass
        
        explaination = soup.find(class_ = 'app_pageContent__PSDsN').find('p').text
        content += f"gate {self.num}: \n\n{explaination}"
        return content

class Center(Stock):
 
    def scrape(self):
        response = requests.get(
            "https://humandesign.tools/hd-centers/" + self.num + "-center")
 
        soup = BeautifulSoup(response.content, "html.parser")
 
        # 爬取卡片資料
        cards = soup.find_all(
            'div', {'class': 'app_pageContent__PSDsN'}, limit=1)
 
        content = f"{self.num} center:\n\n"
        for card in cards:
           pass
        
        tests = soup.find(class_ = 'app_pageContent__PSDsN').find_all('p', limit=2)
        for test in tests:
            content += test.text + "\n\n"
        #explaination = soup.find(class_ = 'app_pageContent__PSDsN').find('p').text
        #content += f"{self.num} center: \n{explaination}\n"
        
        return content

class Profile(Stock):
 
    def scrape(self):
        response = requests.get(
            "https://humandesign.tools/hd-profiles/" + self.num + "-profile")
 
        soup = BeautifulSoup(response.content, "html.parser")
 
        # 爬取卡片資料
        cards = soup.find_all(
            'div', {'class': 'app_pageContent__PSDsN'}, limit=1)
 
        content = f"{self.num} Profile:\n\n"
        for card in cards:
           pass
        
        tests = soup.find(class_ = 'app_pageContent__PSDsN').find_all('p')
        for test in tests:
            content += test.text + "\n\n"
        #explaination = soup.find(class_ = 'app_pageContent__PSDsN').find('p').text
        #content += f"{self.num} center: \n{explaination}\n"
        
        return content