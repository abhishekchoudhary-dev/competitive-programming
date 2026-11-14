# cook your dish here
# Problem: DSA Monday 028 -  Non overlapping prefix suffix
# Problem Link: https://www.codechef.com/problems/NONOVER

from collections import defaultdict
s = input()
mx = 0
left = 0
right = len(s)-1
d = defaultdict(int)
d1 = defaultdict(int)
#dictionary will only have 26 keys so this comparison of dicts is not expensive
# we can also keep freq array with ord values as index
while left<right:
    d[s[left]]+=1
    d1[s[right]]+=1
    if d == d1:
        mx = max(mx,left+1)
    left+=1
    right-=1
    
print(mx)
