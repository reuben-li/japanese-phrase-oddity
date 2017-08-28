# -*- coding: utf-8 -*-
"""natural japanese"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
NGRAM = 3
PHRASE = u'化け物だったか'  # temporary
N = len(list(PHRASE))


def getHits(term):
    """HTTP request to search API"""
    hits = term  # temporary
    return hits


def getCache(term):
    """Check if cache exists"""
    if False:  # temporary
        hits = getHits(term)
        storeCache(term, hits)


def storeCache(term, hits):
    """Add to cache"""
    return True


for i in xrange(N - (NGRAM - 1)):
    print(PHRASE[i: i + NGRAM])
