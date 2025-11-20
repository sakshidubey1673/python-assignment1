# maximum of three number. using ternary operator .

a = 50
b = 30
c = 20

#max = a if (a > b and a > c )else(b if b > c else c)
maxm = a if (b > a and  c > a )else(b if b < c else a)  # CONDITION CHANGE..
print("maximum of three number is -> " , maxm)