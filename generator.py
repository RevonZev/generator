import json5
import random
import os
import platform
import re

import tkinter as tk
from tkinter.filedialog import askopenfile
tk.Tk().withdraw()


def load_data():
    with askopenfile() as f:
        data = f.read()
    data = json5.loads(data)
    return data


def main():
    data = load_data()

    generate(data)


def usr_input_for_reroll():
    usr_input = input('Reroll number? (-2: exit, -1: all) ')

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    if usr_input in ['-2', '']:
        exit()
    elif usr_input == '-1':
        generate(data)
    else:
        return usr_input


def generate(data, generated_data={}, usr_input='0'):
    global falses

    if generated_data == {}:
        for idx, key in enumerate(data.keys()):
            generated_data[str(idx)] = [key, random.choice(data[key])]
    else:
        generated_data[usr_input][1] = random.choice(
            data[generated_data[usr_input][0]])

    falses = []
    filtered_data = {
        key: [
            filter_if(generated_data[key][0], generated_data),
            generated_data[key][1],
        ]
        for key in generated_data.keys()
    }

    for key, value in filtered_data.items():
        if value[0] != 'skip':
            print(key+'.', value[0]+':', value[1])

    usr_input = usr_input_for_reroll()

    generate(data, generated_data, usr_input)


def filter_if(key, generated_data):
    global falses
    if_data = []

    if re.findall(r'if .+ is .+$', key):
        if_data = [re.sub(r'.+ if (.+) is .+$', r'\1', key),
                   re.sub(r'.+ if .+ is (.+)$', r'\1', key),
                   re.sub(r'(.+) if .+ is .+$', r'\1', key)]

    if if_data != []:
        # print(if_data[0], 'xxx', if_data[1], 'xxx', if_data[2])
        for key2, value in generated_data.values():
            if re.findall(r'if .+ is .+$', key2):
                key2 = re.sub(r'(.+) if .+ is .+$', r'\1', key2)

            if if_data[0] == key2 and if_data[1] == value and if_data[0] not in falses:
                return if_data[2]

        falses += [if_data[2]]
        return 'skip'

    return key


if __name__ == '__main__':
    falses = []

    main()
