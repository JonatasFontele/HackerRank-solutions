# 59 characters
# Bit Operator -~i = -(-(i+1)
for i in range(100):print(i%3//2*'Fizz'+i%5//4*'Buzz'or-~i)