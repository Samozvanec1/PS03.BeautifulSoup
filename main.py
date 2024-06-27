from bs4 import BeautifulSoup
import requests


url = "https://quotes.toscrape.com/"

response = requests.get(url) # переменная response получаут данные с помощью метода GET находящегося в библиотеки



print(response.content)
html = response.content # содержимое переменной response присваивается переменной html
soup = BeautifulSoup(html, 'html.parser') # создается переменная soup с помощью библиотеки BeautifulSoup принимающая в качестве аргумента html и указывающая на парсер html

links = soup.find_all('a') # находит все ссылки в html и присваивает их переменной links (список)
for link in links: # цикл для перебора ссылок
    print(link.get('href')) # вывод ссылок в консоль. get('href') - получение атрибута href для каждой ссылки в списке links (список)

# Парсинг это сбор информации по определенным признакам?