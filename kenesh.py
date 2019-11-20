import requests
from pprint import pprint
from bs4 import BeautifulSoup

url = 'http://www.kenesh.kg/ru/deputy/show/51/abdildaev-miktibek-yusupovich'


def get_html(url):
    r = requests.get(url)
    return r.text



def get_urls(html):
    soup = BeautifulSoup(html, 'html.parser')
    tds = soup.find('table', class_='table').find_all('td')
    links = []
    for td in tds:
        a = td.find('a').get('href')      
        link = 'http://www.kenesh.kg' + a
        pprint(link)
        links.append(link)
    return links

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        name = soup.find('h3', class_='deputy-name').text.strip()
        pprint(name)
    except:
        name = ''

    try:
        bio = soup.find('div', id='biography').text.strip()
        print(bio)
    except:
        bio = ''

    try:
        number = soup.find('p', class_= 'mb-10').text.strip()
        print(number)
    except:
        number = ''

def write_csv(data):

def main(): 
    url = 'http://www.kenesh.kg/ru/deputy/list/35'
    links = get_urls(get_html(url))
    for link in links:
        get_data(link)

if __name__ == '__main__':
    main()



