# -*- coding: utf-8 -*-
"""natural japanese"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
NGRAM = 3


def getCount(term):
    """HTTP request to search API"""
    return term

sen = u'化け物だったか'
n = len(list(sen))

for i in xrange(n - (NGRAM - 1)):
    print(sen[i: i + NGRAM])
