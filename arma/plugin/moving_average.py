# coding: utf-8
from collections import defaultdict


class MovingAverage(object):

    def __init__(self, lags=1):
        self.lags = lags
        self._window = defaultdict(list)

    @classmethod
    def create(cls, param):
        lags = int(param.get('lags', 1))
        return cls(lags)

    def extract(self, key, value):
        self._window[key].append(value)
        window = self._window[key]
        if len(window) == self.lags:
            ma = sum(window) / len(window)
            self._window[key].pop(0)
            ret = [(key, ma)]
        else:
            ret = [(key, 0)]
        return ret