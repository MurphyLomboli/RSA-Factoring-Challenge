import sys
import math

def factorize(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return (i, n // i)
    return (n, 1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        for line in f:
            n = int(line.strip())
            p, q = factorize(n)
            print("{}={}*{}".format(n, p, q))
