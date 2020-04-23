s = input()
t = input()

ans = set()
try:
    for i in range(len(s)):
       ans.add(s.index(t,i))
except:
    pass

print(len(ans))


s = input()
t = input()
ans = 0
for i in range(len(s)):
    if s[i:].startswith(t):
        ans += 1

print(ans)