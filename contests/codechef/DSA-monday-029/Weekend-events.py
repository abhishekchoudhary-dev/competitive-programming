# cook your dish here


# Problem: DSA Monday 029 -  Weekend events
# Problem Link: https://www.codechef.com/DSAMONDAY029/problems/WEEKEV

def solve():
    n = int(input())
    events = []
    for _ in range(n):
        s,e,c = map(int,input().split())
        events.append([s,e,c])
    # no sorting just check for each
    #print(events)
    dp = [0] *49
    for t in range(1,49):
        dp[t] = dp[t-1]
        for s,e,c in events:
            if e == t:
                dp[t] = max(dp[t], dp[s]+c)
    print(max(dp))
                
    
    
t = int(input())
for _ in range(t):
    solve()