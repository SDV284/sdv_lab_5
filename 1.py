n = int(input("N = "))

print(f"Введіть {n} чисел:")

arr = [int(input()) for _ in range(n)]
neg_arr = list(filter(lambda x: x < 0, arr))

print("Від'ємні числа: ", neg_arr[::-1])