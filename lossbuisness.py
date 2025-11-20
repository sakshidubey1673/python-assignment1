N=int(input())
r=0
s=0
i=1

while N>0:
 r=r+i*0
 s=s+i*1
 N=N-(i+i*2-1) 
 i=i+1

 if (i-1)*3-2 >= N+1:
  print("Suresh")
 else: 
  print("Ramesh")   
