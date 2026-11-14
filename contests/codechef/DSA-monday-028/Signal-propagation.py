# cook your dish here

# Problem: DSA Monday 028 -  Signal propogation
# Problem Link: https://www.codechef.com/problems/CLNAR

def solve():
    n = int(input())
    strengths = list(map(int,input().split()))
    i = len(strengths) - 2
    seconds = 0
    while i >= 0:
    #for i in range(len(strengths)-2,-1,-1):
        if strengths[i] < strengths[i+1]:
            j = i
            sentinal = strengths[i+1]
            while j >= 0 and strengths[j] < sentinal:
                j-=1
            seconds = max(seconds, i-j)
            i = j
            continue
        i-=1
    print(seconds)
            
    
t = int(input())
for _ in range(t):
    solve()