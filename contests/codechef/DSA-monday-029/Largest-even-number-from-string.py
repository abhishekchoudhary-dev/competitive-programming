# cook your dish her

# Problem: DSA Monday 029 -  Largest even number from string
# Problem Link: https://www.codechef.com/DSAMONDAY029/problems/LAEVNU

s = input()
digits = [int(d) for d in str(s) if '0'<=d<='9']
evens = [k for k in digits if k%2==0]

if not evens:
    print(-1)
elif not digits or sum(digits)==0:
    print(0)
else:
    smallest_even = min(evens)
    digits.sort(reverse= True)
    ans = []
    last_pos = False
    for d in digits:
        if d==smallest_even and not last_pos:
            last_pos = True
        else:
            ans.append(d)
    #ans = [d for d in digits if d!= smallest_even]
    ans.append(smallest_even)
    print(''.join(map(str,ans)))

'''
digits = set()
found_even = False
smallest_even = float('inf')
for ch in s:
    if ch.isdigit():
        if int(ch)%2==0:
            smallest_even = min(smallest_even,int(ch))
            found_even = True
        digits.add(int(ch))
if not found_even or len(digits) == 0:
    print(-1)
elif sum(digits) == 0:
    print(0)
else:
    digits = list(digits)
    digits.sort(reverse=True)
    ans = []
    for d in digits:
        if d == smallest_even:
            continue
        ans.append(d)
    ans.append(smallest_even)
    print(''.join(str(k) for k in ans))
'''