# cook your dish here

# Problem: DSA Monday 029 -  Sentence anagrams
# Problem Link: https://www.codechef.com/DSAMONDAY029/problems/SANAGRA

import re
from collections import Counter

f = input()
s = input()

if not f and not s:
    print("The sentences are anagrams.")
else:
    words1 = re.split(r'[^a-zA-Z]+',f)
    #words1 = [w for w in re.split(r'[^a-zA-Z]+', f) if w]
    words2 = re.split(r'[^a-zA-Z]+',s)
    
    #words2 = [w for w in re.split(r'[^a-zA-Z]+', s) if w]
    d1 = Counter(word.lower() for word in words1 if word)
    d2 = Counter(word.lower() for word in words2 if word)
    if d1==d2:
        print("The sentences are anagrams.")
    else:
        print("The sentences are not anagrams.")