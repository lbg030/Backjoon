zero = [1, 0, 1]
one = [0, 1, 1]

# 22


def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            # print(f"zero = {zero}")
            one.append(one[i-1] + one[i-2])
            # print(f"one = {one}")
    print(f'{zero[num]} {one[num]}')


T = int(input())

for _ in range(T):
    fibonacci(int(input()))