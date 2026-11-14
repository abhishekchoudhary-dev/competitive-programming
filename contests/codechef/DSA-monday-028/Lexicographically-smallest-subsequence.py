# cook your dish here

# Problem: DSA Monday 028 -  Lexicographically smallest subsequence
# Problem Link: https://www.codechef.com/problems/LSMALL

def solve():
    s = input()
    k = int(input())
    n = len(s)
    stack = []
    for i,ch in enumerate(s):
        #pop only when smaller found and enough remain
        while stack and stack[-1]>ch and (len(stack) - 1 + (n-i))>=k:
            stack.pop()
        if len(stack) < k:
            stack.append(ch)
    print(''.join(stack))




t = int(input())
for _ in range(t):
    solve()