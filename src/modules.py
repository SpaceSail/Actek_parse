import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup


def check_url(url: str):
    """Function for a checking "table" attribute availability"""
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    if not soup.find_all('table'):
        for i in soup.find_all('a'):
            if 'https://data' in (i.get('href')):
                return i.get('href')


def get_data(new_url):
    """Function for obtaining data"""
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    new_url = (f'{str(new_url.replace('data', 'dataportal-api'))}api/Day'
               f'AheadPrices?date={date}&market=DayAhead&deliveryArea='
               f'AT&currency=EUR')
    response = requests.get(new_url)
    ans = (response.json()['multiAreaEntries'])
    return ans


def write_to_excel(ans):
    """Function for writing data"""
    norm = pd.json_normalize(ans)
    norm.to_excel('out.xlsx', index=False)


