# consider int val=0xCAFE; Write expression using bitwise operator
# 1. test if atleast  three of last four bits (LSB) are on
# 2. reveerse the byte order (i.e. produce val = 0xFECA)
# 3. rotate four bites (i.e . produce val=0xECFA)

val=0xCAFE
last4 = val & 0xF
c=0
for i in range(4):
 if (last4>>i)&1:
    c+=1
if c>=3:
  print("Atleast 3 bites on")
else:
  print("Less then 3 bites on")

reverse=((val & 0xF0)<<8)|((val>>4)&0x0F0F)
print("rev:",hex(reverse))

rot=((val>>4)&0xFFFF)|(val<<12)
print("rot:",hex(rot)) 

