from math import *
x1,y1,r1,x2,y2,r2= map(int,input().split())
numo = 0
if x1==x2 and y1==y2 and r1==r2:
    numo=-1
if x1+r1>=x2+r2 or x1+r1==x2-r2 or x1-r1==x2+r2 or x1-r1==x2-r2 or y1+r1==y2+r2 or y1+r1==x2-r2 or y1-r1==y2+r2 or y1-r1==y2-r2:
    numo=1

print(numo)