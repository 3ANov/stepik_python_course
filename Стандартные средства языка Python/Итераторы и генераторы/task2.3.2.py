import itertools
import math
a = [i for i in range(5)][1:]
print(a)

def primes():
    i = 2
    while True:
        is_prime = True
        divisor = 2
        while divisor ** 2 <= i:
            if i % divisor == 0:
                is_prime = False # non-trivial divisor
                break

            divisor += 1

        if is_prime:
            yield i

        i += 1



print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]