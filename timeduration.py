n = int(input())
for i in range(n):
  sh, sm, eh, em = map(int,input().split())

  hr = eh - sh
  mn = em - sm
  if mn < 0:
   hr = hr - 1
   mn = mn + 60


   print(hr,mn)   