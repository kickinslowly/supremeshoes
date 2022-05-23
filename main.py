from bs4 import BeautifulSoup
import requests
import time
import http.client, urllib
from pushover import init, Client
from datetime import datetime

# pushover init stuff where app key is mine, client key should be clients but  is currently mine for testing
app_key = 'atu8tzewh473p2ww2vrbg1zyw5aekc'
client_key = 'ug3886f3w48c8o95wiw6bgzagw7o4c'
init(app_key)

# relating to supreme html tag data
style_id = {'data-style-id': '34049'}
sold = 'data-sold-out="true"'

# beautifulsoup pulls data and finds specific tags related to topic, in this case shoes style_id
html_text = requests.get('https://www.supremenewyork.com/shop/shoes/w8fsl0j1g/b0y4ecjmk').text
soup = BeautifulSoup(html_text, 'lxml')
style = soup.find_all('button', attrs=style_id)


# upon these conditions app will fire notification through pushover and do this continuously
while True:
    if style[0]['data-sold-out'] == 'true':
        print('SOLD OUT ' + str(datetime.now()))
    else:
        Client(client_key).send_message('FUCK MESSAGE!', title='TEST TITLE', url='https://www.supremenewyork.com/shop/shoes/w8fsl0j1g/b0y4ecjmk')
        print('SHOES ARE NOT SOLD OUT!!!!  GOOD LUCK BUYING THEM!!!!')
        break
    time.sleep(1)



