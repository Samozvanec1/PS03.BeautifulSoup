
import requests
from bs4 import BeautifulSoup


def get_english_words():  # функция для получения списка английских слов
    url = "https://randomword.com/"  # ссылка на первую страницу сайта
    try:
        response = requests.get(url)  # получаем данные сайта с помощью метода GET из библиотеки requests
        soup = BeautifulSoup(response.content, "html.parser")  # создаем объект BeautifulSoup для парсинга HTML данных

        english_word = soup.find("div", id="random_word").text.strip()  # находим слово по тегу div и id="random_word"
        word_definition = soup.find("div",
                                    id="random_word_definition").text.strip()  # находим определение по тегу div и id="random_word_definition"

        return {
            "english_word": english_word,
            # возвращаем данные в виде словаря с ключами "english_word" и "word_definition"
            "word_definition": word_definition
        }

    except Exception as e:
        print(f"Произошла ошибка: {e}")  # выводит в консоль текст с описанием ошибки


def word_game():
    print("Добро пожаловать в игру 'Слова'")  # выводит в консоль текст "Добро пожаловать в игру 'Слова'"
    while True:
        word_dict = get_english_words()  # получаем данные в виде словаря
        if not word_dict:
            print("Не удалось получить слово. Попробуйте снова.")
            continue

        word = word_dict.get("english_word")  # получаем слово
        word_definition = word_dict.get("word_definition")  # получаем определение

        print(f"Значение слова: {word_definition}")  # выводим определение слова
        user_input = input("Что это за слово? ")  # получаем ввод пользователя

        if user_input.lower() == word.lower():  # если введенное слово соответствует полученному
            print("Верно, ТЫ КРАСАВЧИК!!!")  # выводим сообщение о правильности
        else:
            print(
                f"НЕВЕРНО, ТЫ НЕ КРАСАВЧИК!!! А вот слово было: {word}")  # выводим сообщение о неправильности и правильное слово

        play_again = input("Хочешь ещё? (y/n) ").strip().lower()  # спрашиваем, хочет ли пользователь сыграть снова

        if play_again != "y":  # если ответ не "y"
            print("Спасибо за игру")  # выводим сообщение о завершении игры
            break  # прерываем цикл


            print("Спасибо за игру")  # выводим сообщение о завершении игры
            break  # прерываем цикл
word_game()