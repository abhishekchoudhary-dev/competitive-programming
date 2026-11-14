# update the code below to solve this problem
# Problem: DSA Monday 028 -  Apples and oranges
# Problem Link: https://www.codechef.com/problems/BMC15A
import math

def solve():
    n,m = map(int,input().split())
    print(math.gcd(n,m))
        

t = int(input())
for i in range(t):
    solve()
