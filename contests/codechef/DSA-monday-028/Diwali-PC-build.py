# cook your dish here
# Problem: DSA Monday 028 -  Diwali PC build
# Problem Link: https://www.codechef.com/problems/DIWALIPC
def solve():
    p,d,k,b = map(int,input().split())
    if p+d*k <= b:
        print("YES")
    else:
        print("NO")
    


t = int(input())
for _ in range(t):
    solve()