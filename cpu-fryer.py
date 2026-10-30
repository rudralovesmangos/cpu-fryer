import sys
sys.set_int_max_str_digits(0)
num = 1
while True:
    for i in range(num):
        num += 10000
        num = num * num
        num += 1
        print(f"CPU CALCULATION NUMBER: {num}")
