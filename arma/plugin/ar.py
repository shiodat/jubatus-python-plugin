# coding: utf-8
from collections import defaultdict


class AutoRegressive(object):

    def __init__(self, lags=1):
        self.lags = lags
        self._window = defaultdict(list)

    @classmethod
    def create(cls, param):
        lags = int(param.get('lags', 1))
        return cls(lags)

    def extract(self, key, value):
        if len(self._window[key]) == 0:
            self._window[key] = [0]*self.lags
        self._window[key].append(value)
        self._window[key].pop(0)
        ret = [(u"{}_{}".format(key, t),
               self._window[key][t])
               for t in range(self.lags)]
        ret.append((u"bias", 1))
        return ret

