# cook your dish here
# Problem: DSA Monday 028 -  Largest mischievous group
# Problem Link: https://www.codechef.com/problems/KPITMISCHIEF
n = int(input())
s = input()

runs = []
for i,st in enumerate(s):
    if st=='g':
        continue
    if i>0 and s[i]==s[i-1]:
        runs[-1][1]+=1
    else:
        runs.append([st,1,i])

start = end = 0
mx = 0
for run in runs:
    if run[1] > mx:
        mx = run[1]
        start = run[2]
        end = run[2]+run[1]-1
print(start, end)