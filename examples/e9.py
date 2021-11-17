#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Операция tuple()
    # 1. Создание кортежа из слова 'Hello'
    d = tuple('Hello')  # d = ('H', 'e', 'l', 'l', 'o')
    # 2. Создание кортежа из списка
    # Заданный список
    lst = [2, "abc", 3.88]
    # Создать кортеж
    e = tuple(lst)  # e = (2, 'abc', 3.88)
    # 3. Создание кортежа из другого кортежа
    f = tuple((3, 2, 0, -5))  # f = (3, 2, 0, -5)
    print(f"d = {d}")
    print(f"e = {e}")
    print(f"f = {f}")
