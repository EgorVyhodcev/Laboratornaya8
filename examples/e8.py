#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    (a, b, c) = (1, 2, 3)
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    a = 100
    b = 'foo'
    (a, b) = (b, a)
    print(f"a = {a}")
    print(f"b = {b}")
