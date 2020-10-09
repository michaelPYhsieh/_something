# https://www.ptt.cc/bbs/Python/M.1602060224.A.B1E.html

def helper(arr, num):
    subs = {()}
    for a in arr:
        subs |= { s + (a, ) for s in subs }
    re = []
    for _ in subs:
      if sum(_) == num:
        re.append(_)
    return re

t = [821,225,1821,38,1888,843,1517,143,43,16,1120,1714]
num = 2018


rt = helper(t, num)
print(rt)
