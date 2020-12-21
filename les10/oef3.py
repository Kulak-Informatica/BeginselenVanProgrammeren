# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:06:58 2020

@author: Thibaut
"""

def h(s,l,n):
    if len(s) == 0:
        return l*(2**n)
    if s[0] != l:
        return l*(2**n) + h(s[1:],s[0],1)
    return h(s[1:],l,n+1)

def g(s):
    n = 0
    l = ""
    res = ""
    for c in s:
        if c != l:
            res += l*(2**n)
            l = c
            n = 1
        else:
            n += 1
    res += l*(2**n)
    return res

print(h("","",0))
print(h("ab","",0))
print(h("abbcccdddd","",0))
print(h(h(h("_","",0),"",0),"",0))

print(g(""))
print(g("ab"))
print(g("abbcccdddd"))
print(g(g(g("_"))))

"""
print(h([],0,0))
print(h([1,2,3],0,0))
print(h([1,2,2,3],0,0))
print(h([1,3],0,0))
print(h([2,2],0,0))
print(h(h(h("_","",0),"",0),"",0))
"""