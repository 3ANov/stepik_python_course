import sys

str_s = 'ababa'
str_a = 'a'
str_b = 'b'
str_s = str_s.replace(str_a, str_b)


# str_s = str(input())
# str_a = str(input())
# str_b = str(input())

str_s = 'ababa'
str_a = 'ab'
str_b = 'ba'

iterations = 0


def num_change(s, a, b):
    global iterations
    if a in b and a in s:
        return "Impossible"
    if a not in s:
        return 0
    num_change(s.replace(a, b), a, b)
    iterations += 1
    return iterations

#ох уж эти рекурсии


print(num_change(str_s, str_a, str_b))

