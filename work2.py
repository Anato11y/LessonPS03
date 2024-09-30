import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаём объект переводчика
translator = Translator()

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_word = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Переводим слово и определение на русский
        translated_word = translator.translate(english_word, dest="ru").text
        translated_definition = translator.translate(word_definition, dest="ru").text

        # Чтобы программа возвращала словарь
        return {
            "english_word": english_word,
            "translated_word": translated_word,
            "translated_definition": translated_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру!")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        if not word_dict:
            continue

        original_word = word_dict.get("english_word")
        translated_word = word_dict.get("translated_word")
        translated_definition = word_dict.get("translated_definition")

        # Начинаем игру
        print(f"Значение слова - {translated_definition}")
        user = input("Какое это слово на русском? ")
        if user.lower() == translated_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный. Было загадано слово '{translated_word}' (английское слово: {original_word})")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n: ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break


# Запуск игры
word_game()
