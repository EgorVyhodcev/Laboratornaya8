#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Операция [i:j] - взятие среза
    # 1. Кортеж, содержащий целые числа
    A = (0, 1, 2, 3)
    item = A[0:2]  # item = (0, 1)
    print(f"item = {item}")
    # 2. Кортеж, содержащий список
    A = (2.5, ['abcd', True, 3.1415], 8, False, 'z')
    item = A[1:3]  # item = (['abcd', True, 3.1415], 8)
    print(f"item = {item}")
    # 3. Кортеж, содержащий вложенный кортеж
    A = (3, 8, -11, "program")
    B = ("Python", A, True)
    item = B[:3]  # item = ('Python', (3, 8, -11, 'program'), True)
    print(f"item = {item}")
    item = B[1:]  # item = ((3, 8, -11, 'program'), True)
    print(f"item = {item}")
