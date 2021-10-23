#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    i = 0
    for index, el in enumerate(A):
        k = A.count(el)
        if k == 2:
            if len(A) > index + 1:
                if A[index + 1] == el:
                    i = index + 1
                    break
                else:
                    continue
    if i:
        for index, el in enumerate(A):
            if i < index < len(A):
                print(el, end=' ')
    else:
        print("There are no pairs of similar adjacent elements!")
