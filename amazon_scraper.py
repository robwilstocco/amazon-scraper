import requests
from bs4 import BeautifulSoup
import xlwt
import time

URL = 'https://www.amazon.com.br/s?k=iphone&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2'
headers = {
  "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

try:
  
  wb = xlwt.Workbook()
  ws = wb.add_sheet('Iphone Prices')
  ws.write(0,0,"Product")
  ws.write(0,1,"Price")
  row = 1
  col = 0
  
  for products in soup.find_all('div',attrs={'class': 'a-section a-spacing-medium'}):
    
    get_title = products.find('span',attrs={'class': 'a-size-base-plus a-color-base a-text-normal'})
    get_price = products.find('span',attrs={'class': 'a-price-whole'})
    
    time.sleep(0.5)
    
    title = get_title.get_text() if get_title != None else "Produto sem título!"
    price = get_price.get_text().replace(',','') if get_price != None else "Produto sem preço!"

    if 'IPHONE' in title.upper():
      ws.write(row,col,title)
      ws.write(row,col+1,price)
      row = row + 1
  
  wb.save('iphone.xls')
  
except:
  print('An exception occurred')