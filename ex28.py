# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# 2 2
# 4

def rec_sum(a, b):
    if b == 0:
        return a
    return rec_sum(a + 1, b - 1)


a, b = int(input("Введите число A: ")), int(input("Введите число B: "))

print(rec_sum(a, b))
