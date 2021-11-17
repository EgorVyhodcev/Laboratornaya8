#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    print(type(lst))
    print(lst)
    tpl = tuple(lst)
    print(type(tpl))
    print(tpl)
    # Обратная операция также является корректной.
    tpl = (2, 4, 6, 8, 10)
    print(type(tpl))
    print(tpl)
    lst = list(tpl)
    print(type(lst))
    print(lst)
