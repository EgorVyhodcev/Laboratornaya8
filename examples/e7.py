#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    name_and_age = ('Bob', 42)
    (name, age) = name_and_age
    print(f"name = {name}")
    print(f"age = {age}")
    (a,) = (42,)
    print(f"a = {a}")
