# cook your dish here

# Problem: DSA Monday 029 -  Word guess
# Problem Link: https://www.codechef.com/DSAMONDAY029/problems/WOGUE

def solve():
    s = input()
    r = input()
    
    m = []
    for i in range(len(s)):
        if s[i]==r[i]:
            m.append('G')
        else:
            m.append('B')
    print(''.join(m))
        




t = int(input())
for _ in range(t):
    solve()