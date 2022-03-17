#22864
a, b, c, m = map(int, input().split())
s = 0
ans = 0
for i in range(24):
    if s<=m-a:
        s += a
        ans += 1
    else:
        s = max(0, s-c)
print(ans*b)
