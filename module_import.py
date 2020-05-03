
import os # импорт всего модуля

from os import mkdir # импортирование отдельной функции

from os import rmdir as remover

from os import * # мпортирование модуля целиком

# remover('test')

# mkdir('test')

remover('test')

print(os. getcwd())

print(list(walk(getcwd())))