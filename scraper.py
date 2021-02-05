import requests
import PySimpleGUI as window
from bs4 import BeautifulSoup

drug_name = str(input('ჩაწერეთ წამლის სახელი ქართულად: '))
print('გთხოვთ მოიცადოთ, მიმდინარეობს წამლის ძიება...')

# Search for the drug on vidal's search page and get a BS4 Object from the source
search_page = requests.get(f'http://www.vidal.ge/search?query={drug_name}')
soup = BeautifulSoup(search_page.text, 'html.parser')

try:
    # Search for the drug's URL and get a BS4 object from it
    page_caption = soup.find('figcaption', class_ = 'col-xs-10').h6.a
    drug_link = page_caption.get('href')
    drug_page = requests.get(drug_link)
    soup = BeautifulSoup(drug_page.text, 'html.parser')

    # Scrape text from the page
    general_info = soup.find('div', class_ = 'col-xs-12 col-sm-7 p_x_0').get_text()
    detailed_info = soup.find('figcaption', class_ = 'item-info').get_text()

    print('წამალი მოიძებნა!')

    # GUI
    window.popup_scrolled(general_info, detailed_info)

except Exception:
    print('წამალი ვერ მოიძებნა')
