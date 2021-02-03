import requests
from bs4 import BeautifulSoup
import PySimpleGUI as window

DrugName = str(input('ჩაწერეთ წამლის სახელი ქართულად: '))
print('გთხოვთ მოიცადოთ, მიმდინარეობს წამლის ძიება...')

#Firstly we search for drug on vidals search page and then we convert that to content
SearchPage = requests.get(f'http://www.vidal.ge/search?query={DrugName}')
SearchPageContent = BeautifulSoup(SearchPage.content, 'html.parser')

try:
    #Then we search for Drug URL, go to that link and convert that into content
    PageCaption = SearchPageContent.find('figcaption', class_ = 'col-xs-10').h6.a
    DrugLink = PageCaption.get('href')
    DrugPage = requests.get(DrugLink)
    DrugPageContent = BeautifulSoup(DrugPage.content, 'html.parser')

    #Then we scrape text from that page
    GeneralInfo = DrugPageContent.find('div', class_ = 'col-xs-12 col-sm-7 p_x_0').get_text()
    DetailedInfo = DrugPageContent.find('figcaption', class_ = 'item-info').get_text()

    print('წამალი მოიძებნა!')

    #GUI
    window.popup_scrolled(GeneralInfo, DetailedInfo)

except Exception:
    print('წამალი ვერ მოიძებნა')



