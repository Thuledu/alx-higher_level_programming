#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

a = 10
b = 5

add_result = add(a, b)
subtract_result = sub(a, b)
multiply_result = mul(a, b)
divide_result = div(a, b)

print("{:a} + {:b} = {:d}".format(a, b, add_result))
print("{:a} - {:b} = {:d}".format(a, b, subtract_result))
print("{:a} * {:b} = {:d}".format(a, b, multiply_result))
print("{:a} / {:b} = {:d}".format(a, b, divide_result))
