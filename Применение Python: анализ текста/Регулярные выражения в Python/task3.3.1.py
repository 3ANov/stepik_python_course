import re

# pattern = r"a[abc]c"
# string = "acc"
#
# match_object = re.search(pattern, string)
# print(match_object)
#
# string = "abc, acc, aac"
# all_inclusions = re.findall(pattern, string)
# print(all_inclusions)
#
# fixed_typos = re.sub(pattern, "abc", string)
# print(fixed_typos)
#
# put your python code here
import re
import sys

for line in sys.stdin:
    line = line.strip()
    print(int(line, 2))