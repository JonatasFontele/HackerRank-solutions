# 61 characters
i=1
while i<101:print("Fizz"*(i%3<1)+"Buzz"*(i%5<1)or i);i+=1

# 59 characters
# Bit Operator -~i = -(-(i+1)
for i in range(100):print(i%3//2*'Fizz'+i%5//4*'Buzz'or-~i)