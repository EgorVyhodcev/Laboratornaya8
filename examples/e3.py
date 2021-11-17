#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = ()
    print(type(a))
    b = tuple()
    print(type(b))
    a = (1, 2, 3, 4, 5)
    print(type(a))
    print(a)
    a = tuple([1, 2, 3, 4])
    print(a)
    not_a_tuple = (42)
    tpl = (42,)
    print(type(not_a_tuple))
    print(type(tpl))
