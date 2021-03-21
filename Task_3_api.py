"""
Task 3: Мы сохраняем время присутствия каждого пользователя на уроке
виде интервалов. В функцию передается словарь, содержащий три списка с
таймстемпами (время в секундах):
— lesson – начало и конец урока
— pupil – интервалы присутствия ученика
— tutor – интервалы присутствия учителя
Интервалы устроены следующим образом – это всегда список из четного
количества элементов. Под четными индексами (начиная с 0) время входа на
урок, под нечетными - время выхода с урока.
Нужно написать функцию, которая получает на вход словарь с интервалами и
возвращает время общего присутствия ученика и учителя на уроке (в секундах).
Будет плюсом: Написать WEB API с единственным endpoint’ом для вызова этой
функции.

"""

import ast
import logging

from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s, %(message)s'))
logger.addHandler(handler)


def appearance(intervals):
    intervals = ast.literal_eval(intervals)
    new_lesson = []
    for il, l in enumerate(intervals['lesson']):
        if il % 2 == 0:
            new_lesson += list(range(l, intervals['lesson'][il+1]))

    new_pupil = []
    for ip, p in enumerate(intervals['pupil']):
        if ip % 2 == 0:
            new_pupil += list(range(p, intervals['pupil'][ip+1]))

    new_tutor = []
    for it, t in enumerate(intervals['tutor']):
        if it % 2 == 0:
            new_tutor += list(range(t, intervals['tutor'][it+1]))

    counter = 0
    for x in new_tutor:
        if (x in new_pupil) and (x in new_lesson):
            counter += 1

    logger.info(counter)
    return str(counter)


@app.route('/time', methods=['GET'])
def api_id():
    if 'id' in request.args:
        intervals = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    return appearance(intervals)


if __name__ == '__main__':
    app.run()
