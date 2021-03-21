""""
Task 1: Дан массив чисел, состоящий из некоторого количества подряд
идущих единиц, за которыми следует какое-то количество подряд идущих нулей:
111111111111111111111111100000000. Найти индекс первого нуля (то есть найти
такое место, где заканчиваются единицы, и начинаются нули)

Какова сложность вашего алгоритма?

def task(array):
  pass

print(task("111111111111111111111111100000000"))
# >> OUT: 25...

"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


def main():
    logger.debug('logging is started')
    string = '111111111111111111111111100000000'
    start_0 = string.find('0')
    logger.debug(start_0)
    print(start_0)


if __name__ == '__main__':
    main()
