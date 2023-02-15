# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def rec_pow(input_number, power_cout):
    if power_cout == 1:
        return input_number
    return rec_pow(input_number, power_cout - 1) * input_number


a, b = int(input("Введите число A: ")), int(input("Введите число B: "))

print(rec_pow(a,b))
