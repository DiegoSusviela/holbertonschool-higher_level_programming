#!/usr/bin/python3
"""
Once per Trial, hooking a Survivor while Blood
Warden is active calls upon The Entity to block
the exits for all Survivors for 30/40/60 seconds.
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

    def existe(y):
        """determines if wopa omegalul"""
        for x in range(num):
            if y == aux[x][1]:
                return True
        return False

    def nope(x, y):
        """determines if wopa omegalul"""
        if (existe(y)):
            return False
        i = 0
        while(i < x):
            if abs(aux[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def rem(x):
        for i in range(x, num):
            aux[i][1] = None

    def nqueens(x):
        """determines if wopa omegalul"""
        for y in range(num):
            rem(x)
            if nope(x, y):
                aux[x][1] = y
                if (x == num - 1):
                    print(aux)
                else:
                    nqueens(x + 1)

    nqueens(0)
