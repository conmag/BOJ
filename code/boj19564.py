# https://www.acmicpc.net/problem/19564
s = input()
ans = 1
for i in range(1,len(s)):
    if s[i-1]>=s[i]:
        ans += 1
print(ans)
