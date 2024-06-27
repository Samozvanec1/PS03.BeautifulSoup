import requests
from bs4 import BeautifulSoup




def get_english_words():  # функция для получения списка английских слов
    url = "https://randomword.com/"  # ссылка на первую страницу сайта
    try:  # пытаемся выполнить код в блоке try в случае возникновения ошибки в блоке except иначе выполняем код в блоке finally
        response = requests.get(url)  # получаем данные сайта с помощью метода GET из библиотеки requests
        soup = BeautifulSoup(response.content, "html.parser")  # создаем объект BeautifulSoup для парсинга HTML данных с помощью библиотеки BeautifulSoup
        english_words = soup.find("div", id = "random_word").text.strip()  # находимируемся по html и находимируемся по тегу div и внутри него наNavigируемся по тегу id = "random_word"
        word_defenition = soup.find("div", id = "random_word_definition").text.strip()    # наNavigируемся по html и наNavigируемся по тегу div и внутри него наNavigируемся по тегу cid = "random_word_definition"

        return {
            "english_word": english_words,  # получаем  данные в виде словаря с ключами "english_word" и "word_defenition"
            "word_defenition": word_defenition # получаем данные в виде словаря с ключами "english_word" и "word_defenition"
        }

    except Exception as e:
        print(f"Произошла ошибка,      внимательнее {e}")  # выводит в консоль текст "Произошла ошибка, внимательнее"

def word_game():
    print("Добро пожаловать в игру 'Слова'")  # выводит в консоль текст "Добро пожаловать в игру 'Слова'"
    while True:
       word_dict = get_english_words()  # получаем данные в   виде словаря с ключами "english_word" и "word_defenition"
       word = word_dict.get("english_word")  # получаем данные в виде словаря с ключами "english_word" и "word_defenition"
       word_defenition = word_dict.get("word_defenition")  # получаем данные в виде словаря с ключами "english_word" и "word_defenition"

       print(f"Значение  сдова: {word_defenition}")  # выводит в консоль текст "Значение  сдова: {word_defenition}"
       user = input("Что это за слово ")  # выводит в консоль текст "Что это за слово " и получает данные в переменную user

       if user == word:  # если user равен word
           print("Верно, ТЫ КРАСАВЧИК!!!")  # выводит в консоль текст "Верно, ТЫ КРАСАВЧИК!!!"
       else:
           print(f"НЕВЕРНО, ТЫ НЕ КРАСАВЧИК!!! А вот слово было: {word}")  # выводит в консоль текст "НЕВЕРНО, ТЫ НЕ КРАСАВЧИК!!! А вот слово было: {word}"
       play_again = input("Хочешь ещё? (y/n) ")  # выводит в консоль текст "Хочешь ещё? (y/n) " и получает данные в переменную play_again

       if play_again != "y":  # если play_again не равен "y"
           print("Спасибо за игру")  # выводит в консоль текст "Спасибо за игру"
           break  # прерывает цикл while True (цикл вложенный)

word_game()