#!/usr/bin/python3
"""
As soon as at least one Exit Gate is opened, Blood Warden activates.
The Auras of Survivors standing within the Exit-Gate area are revealed to you.

Once per Trial, hooking a Survivor while Blood Warden is active
calls upon The Entity IconHelp entity.png to block the exits
for all Survivors for 30/40/60 seconds. 
"""


from sys import argv

if __name__ == "__main__":
    aux = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    num = int(argv[1])
    if num < 4:
        print("N must be at least 4")
        exit(1)

    for i in range(num):
        aux.append([i, None])

    def already_exists(y):
        for x in range(num):
            if y == aux[x][1]:
                return True
        return False

    def reject(x, y):
        if (already_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(aux[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        for i in range(x, num):
            aux[i][1] = None

    def nqueens(x):
        for y in range(num):
            clear_a(x)
            if reject(x, y):
                aux[x][1] = y
                if (x == num - 1):
                    print(aux)
                else:
                    nqueens(x + 1)

    nqueens(0)
