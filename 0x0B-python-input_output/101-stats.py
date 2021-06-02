#!/usr/bin/python3
"""akj bsdjkansd klna;lsd"""


import sys

size = 0
status_code = {"200": 0, "301": 0,
               "400": 0, "401": 0,
               "403": 0, "404": 0,
               "405": 0, "500": 0}
cont = 0
try:
    for line in sys.stdin:
        splits = line.split()
        if len(splits) > 1:
            aux = cont
            if splits[-2] in status_code:
                status_code[splits[-2]] += 1
                cont += 1
            try:
                size += int(splits[-1])
                if aux == cont:
                    cont += 1
            except:
                if aux == cont:
                    continue
        if cont % 10 == 0:
            print("File size: {:d}".format(size))
            for key, value in sorted(status_code.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(size))
    for key, value in sorted(status_code.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(size))
    for key, value in sorted(status_code.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
