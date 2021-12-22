import datetime
import os
import re
from os import listdir, system
from os.path import isfile, join
import urllib.request
from dotenv import load_dotenv

load_dotenv()

files = [f for f in listdir('.') if isfile(join('.', f))]
python_files = [f.replace('.py', '') for f in files if '.py' in f]
day_files = [int(f) for f in python_files if re.search('[0-9]', f) is not None]
current_file = max(day_files)
current_day = datetime.datetime.now().day

if current_day != current_file + 1 :
    file_created = input('Numéro du jour ?')
else:
    file_created = current_day

if int(file_created) in day_files:
    raise FileExistsError(f'Le fichier {file_created}.py existe déjà')


with open(str(file_created) + '.py', 'w', encoding='utf-8') as py_file:
    py_file.write(f'''from tictoc import tic, toc
from cprint import cprint
from collections import defaultdict, Counter

tic()

with open("input{file_created}.txt") as file:
    inp = [line for line in file]
# print(inp)

# -------- Part 1 -----------
print('   PART 1')


toc('Partie 1 terminée en')
# -------- Part 2 -----------
print('   PART 2')


toc('Partie 2 terminée en')''')

system(fr'D:\Users\simar\AppData\Local\JetBrains\Toolbox\apps\PyCharm-P\ch-0\213.5744.248\bin\pycharm64.exe --line 6 {file_created}.py')

COOKIE = os.getenv('COOKIE')
URL = f'https://adventofcode.com/2021/day/{file_created}/input'
req = urllib.request.Request(URL)
req.add_header('Cookie', 'session=' + COOKIE)
data = urllib.request.urlopen(req).read()


with open(f'input{file_created}.txt', 'wb') as input_file:
    input_file.write(data)

system(fr'D:\Users\simar\AppData\Local\JetBrains\Toolbox\apps\PyCharm-P\ch-0\213.5744.248\bin\pycharm64.exe --line 6 input{file_created}.txt')

with open(f'ex{file_created}.txt', 'w', encoding='utf-8') as ex_file:
    ex_file.write('\n')

system(fr'D:\Users\simar\AppData\Local\JetBrains\Toolbox\apps\PyCharm-P\ch-0\213.5744.248\bin\pycharm64.exe --line 6 ex{file_created}.txt')
