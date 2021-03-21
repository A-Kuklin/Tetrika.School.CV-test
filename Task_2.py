"""
Task 2: В нашей школе мы не можем разглашать персональные данные
пользователей, но чтобы преподаватель и ученик смогли объяснить нашей
поддержке, кого они имеют в виду (у преподавателей, например, часто учится
несколько Саш), мы генерируем пользователям уникальные и легко произносимые
имена. Имя у нас состоит из прилагательного, имени животного и двузначной
цифры. В итоге получается, например, "Перламутровый лосось 77". Для
генерации таких имен мы и решали следующую задачу:
Получить с русской википедии список всех животных (Категория:Животные по
алфавиту) и вывести количество животных на каждую букву алфавита. Результат
должен получиться в следующем виде:
А: 642
Б: 412
В:....

"""

import logging

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s, %(message)s'))
logger.addHandler(handler)


def create_list():
    """ creating the list of animals in Task_2.txt """
    S = requests.Session()
    URL = 'https://ru.wikipedia.org/w/api.php'
    str_cont = ''
    list_of_names = []
    while True:

        PARAMS = {
            'action': 'query',
            'format': 'json',
            'list': 'categorymembers',
            'cmtitle': 'Категория:Животные_по_алфавиту',
            'cmlimit': 500,
            'cmcontinue': str_cont,
        }

        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()
        if ('warnings' or 'errors') in DATA:
            logger.error(DATA['warnings'])

        for i in list(DATA['query']['categorymembers']):
            list_of_names.append(i['title'])

        if 'continue' in DATA:
            str_cont = DATA['continue']['cmcontinue']
        else:
            break
    file = open('Task_2.txt', 'w')
    file.write(str(list_of_names))
    file.close()


def main():
    # calling the list(.txt) creation function
    create_list()

    # reading the file with the list of animals
    file_r = open('Task_2.txt')
    list_names = file_r.read()
    file_r.close()

    logger.debug(list_names)
    logger.debug(len(list_names))

    # creating russian alphabet
    a = ord('а')
    before_e = [chr(i) for i in range(a, a + 6)]
    after_e = [chr(i) for i in range(a + 6, a + 32)]
    alphabet = ''.join(before_e + [chr(a + 33)] + after_e)

    # creating a dict with the number of animals for each letter
    letter_dict = {}
    for letter in alphabet.upper():
        counter = 0
        for i in list_names:
            if i[0] == letter:
                counter += 1
                letter_dict[letter] = counter

    logger.debug(letter_dict)

    # printing the result
    for key in letter_dict:
        print(f'{key}: {letter_dict[key]}')


if __name__ == '__main__':
    main()
