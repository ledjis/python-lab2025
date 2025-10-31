# Робота з текстом. Напишіть функцію, яка приймає рядок як вхідні дані та повертає словник,
# де ключі - це унікальні слова в рядку, а значення - кількість їх появ.Створіть та виведіть
# на екран список, де зберігаються слова, що зустрічаються більше 3 разів.

def word_count(text):
    text = text.lower()
    words = text.split()
    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    frequent_words = [word for word, count in word_dict.items() if count > 3]
    print(frequent_words)


text_input = "red blue green red yellow red blue green red blue blue green yellow green blue red yellow green"
word_count(text_input)
