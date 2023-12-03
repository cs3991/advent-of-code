import datetime
import os
import re
import urllib.request
from os import listdir, system
from os.path import isfile, join
from dotenv import load_dotenv

load_dotenv()

current_year = datetime.datetime.now().year
os.chdir(f'./{current_year}')

files = [f for f in listdir(f'.') if isfile(join('.', f))]
python_files = [f.replace('.py', '') for f in files if '.py' in f]
day_files = [int(f) for f in python_files if re.search('[0-9]', f) is not None]
if len(day_files) == 0:
    day_files = [0]
current_file = max(day_files)
current_day = datetime.datetime.now().day

if current_day != current_file + 1:
    day_to_generate = int(input('Numéro du jour ?'))
else:
    day_to_generate = current_day

file_created = f'{day_to_generate:02d}'

if int(file_created) in day_files:
    raise FileExistsError(f'Le fichier {file_created}.py existe déjà')

print(file_created)

with open(str(file_created) + '.py', 'w', encoding='utf-8') as py_file:
    py_file.write(f'''from tictoc import tic, toc
from cprint import cprint
from collections import defaultdict, Counter


with open("ex{file_created}.txt") as file:
    ex = [line for line in file]

with open("input{file_created}.txt") as file:
    inp = [line for line in file]
# print(inp)

tic()
# -------- Part 1 -----------
print('   PART 1')


toc('Part 1 done in')
# -------- Part 2 -----------
print('   PART 2')


toc('Part 2 done in')''')

system(
    fr'"C:\Users\simar\AppData\Local\JetBrains\Toolbox\apps\PyCharm-C\ch-0\232.10227.11\bin\pycharm64.exe" --line 16 {file_created}.py')

COOKIE = os.getenv('COOKIE')
URL = f'https://adventofcode.com/{current_year}/day/{file_created}/input'
req = urllib.request.Request(URL)
req.add_header('Cookie', 'session=' + COOKIE)
data = urllib.request.urlopen(req).read()

with open(f'input{file_created}.txt', 'wb') as input_file:
    input_file.write(data)

system(
    fr'"C:\Users\simar\AppData\Local\JetBrains\Toolbox\apps\PyCharm-C\ch-0\232.10227.11\bin\pycharm64.exe" input{file_created}.txt')

with open(f'ex{file_created}.txt', 'w', encoding='utf-8') as ex_file:
    ex_file.write('\n')

system(
    fr'"C:\Users\simar\AppData\Local\JetBrains\Toolbox\apps\PyCharm-C\ch-0\232.10227.11\bin\pycharm64.exe" ex{file_created}.txt')
