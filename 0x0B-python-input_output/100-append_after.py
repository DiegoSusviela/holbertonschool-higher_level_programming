#!/usr/bin/python3
"""read_file function"""


def append_after(filename="", search_string="", new_string=""):
    """omegalul epa"""
    with open(filename, 'r', encoding='utf-8') as f:
        lista = []
        while True:
            linea = f.readline()
            if linea == "":
                break
            lista.append(linea)
            if search_string in linea:
                lista.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lista)
