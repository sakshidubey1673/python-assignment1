num = int(input())
for i in range(num):
 x,y = map(int,input().split())
 a=x
 b=y
 while b!=0:
  temp = b
  b = a % b
  a = temp

  gcd = a
  print(gcd)   