#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def main(p, randomlist):
    A = []
    for r in randomlist:
        if r < p[0]:
            x = 0
        elif r < p[1]:
            x = 1
        elif r < p[2]:
            x = 2
        else:
            x = 3
        A.append(x)
    return A


def main1(p, randomlist):
    return [len([i for i in p if r > i]) for r in randomlist]


if __name__ == '__main__':
    p = [0.85, 0.92, 0.99, 1]
    r = [random.random() for i in range(100)]
    l1 = main(p, r)
    l2 = main1(p, r)
    print(l1)

    print(l2)

    print(l1 == l2)
