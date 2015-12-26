#!/usr/bin/env python
# coding:UTF-8
"""
共通処理関数を記述します
"""

def toHms(t):
    h = t / 3600
    m = (t % 3600) / 60
    s = t % 60
    hms = str(h) + u"時間" + str(padZero(m)) + u"分" + str(padZero(s)) + u"秒"
    return hms


def toHm(t):
    h = t / 3600
    m = (t % 3600) / 60
    hm = str(h) + u"時間" + str(padZero(m)) + u"分"
    return hm


def padZero(v):
    if (v < 10):
        return "0" + str(v)
    else:
        return str(v)
        