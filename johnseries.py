a = int(input("enter the first value :"))
d = int (input("enter the difference :"))
n = int(input("enter the value of n :"))

ant = a + (n - 1) * d
print("the nth value is ->",ant)

snt = (n * (2 * d + (n - 1) * d) // 2)
print("the sum of nth term is ->",snt)