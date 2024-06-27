from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/page/1/" # ссылка на первую страницу сайта

response = requests.get(url) # получаем данные сайта с помощью метода GET из библиотеки requests
html = response.text # преобразовываем полученные данные в текст
soup = BeautifulSoup(html, 'html.parser') # создаем переменную soup с помощью библиотеки BeautifulSoup

#text = soup.find('span', class_="text") # находимируемся по html и находимируемся по тегу span и внутри него находимируемся по тегу class_='text'
#find_all ищет все элементы и возвращает их в виде списка.  find ищет первый элемент (первый попавшийся0 и возвращает его.
text = soup.find_all('span', class_="text") # находимируемся по html и находимируемся по тегу span и внутри него наNavigируемся по тегу class_='text'
print(text)

author = soup.find_all('small', class_="author")
print(author)

for i in range(len(text)): # цикл, который проходит по количеству элементов в списке text. len(text) - количество элементов в списке
    print(f"Цитата номер {i+1}:") # выводит в консоль текст "Цитата номер" и i+1 (порядковый номер цитаты)
    print(text[i].text) # text[i] - элемент списка text, который имеет индекс i (по порядку) и выводится в консоль
    print(author[i].text) # author[i] - элемент списка author, который имеет индекс i (по порядку) и выводится в консоль
    print(f"Автор цитаты: {author[i].text}\n") # выводит в консоль текст "Автор цитаты" и author[i].text (имя автора цитаты)
