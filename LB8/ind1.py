#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    a = tuple(map(int, input().split()))
    i = 0
    for index, el in enumerate(a):
        k = a.count(el)
        if k > 2:
            if len(a) > index + 1:
                if a[index + 1] == el:
                    i = index + 1
                    break
                else:
                    continue
    if i:
        for index, el in enumerate(a):
            if i < index < len(a):
                print(el, end=' ')
    else:
        print("There are no pairs of similar adjacent elements!")
