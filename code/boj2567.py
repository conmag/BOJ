"""
도화지 100*100 -> 102*102
(why? 끝면은 비교 불가)
색종이 10*10
왼쪽 아래 모퉁이의 x,y좌표
종이를 (x+1,y+1) 도화지에 붙인다
이중 for 문 2번 돌면서
변하는 순간 ans + 1 한다 
for 문의 시작점을 1이어야 한다 
(i-1과 i를 비교하기 때문에)
행과 열을 돌면서 모든 모서리를 체크한다
ans출력
"""

n = 102
a = [[0]*n for _ in range(n)]
m = int(input())
for i in range(m):
    x,y = map(int, input().split())
    for r in range(x,x+10):
        for c in range(y,y+10):
            a[r][c] = 1
ans = 0
for r in range(0,102):
    for c in range(1,102):
        if a[r][c-1]!=a[r][c]:
            ans += 1 
for c in range(0,102):
    for r in range(1,102):
        if a[r-1][c]!=a[r][c]:
            ans += 1
print(ans)     
       
