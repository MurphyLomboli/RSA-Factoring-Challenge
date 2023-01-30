import sys
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def factorize(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return (i, n // i)
    return None

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        for line in f:
            n = int(line.strip())
            p, q = factorize(n)
            if p is None:
                print("No prime factors found for {}".format(n))
            else:
                print("{}={}*{}".format(n, p, q))
