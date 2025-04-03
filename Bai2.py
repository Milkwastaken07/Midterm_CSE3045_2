import math

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Nhập số từ người dùng
n = int(input("Nhập số n nguyên không âm: "))

if n < 0:
    print("n phải là một số nguyên không âm.")
else:
    print(f"{n}! = {factorial(n)}")