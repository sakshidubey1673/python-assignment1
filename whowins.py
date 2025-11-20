rameshcount = 0
sureshcount = 0
n = 10
rem = n      # reamaning value

for i in range(1, n):
     print(i)
     if rem <=0:
       break
     #ramesh
     # rameshcount += i
     print('ramesh turnr'+str(i))

     rem = rem - i
     if rem <= 0:
       print('ramesh last')
       break

     # suresh
     # sureshcount += i + 2
     print('suresh turnr'+str(i+2))

     rem = rem - 2*i
     if rem <= 0:
       print('suresh last')
       break 
  
