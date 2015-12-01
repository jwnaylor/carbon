import unittest
import itertools
import random
import time
from collections import deque

# Python 2.7

random.seed(time.time())

# configuration
MAX_LENGTH=5000
MAX_HIT_RATE=67.0

def palindromes(seed):
    """
    Generates random palindromes using the characters in the seed string.
    Starts by generating palindromes of length 1, increasing stepwise in length
     up to a maximum length of MAX_LENGTH
    Does not attempt to generate all possible palindromes of particular length, but moves on to the next
     possible length when the rate of production of new random palindromes drops below threshold (1/MAX_HIT_RATE)

    Some configuration is possible:
    - MAX_LENGTH upper bound on the length a palindrome, adjust be slightly larger than sampling size
    - MAX_HIT_RATE can be adjusted up to produce a more dense distribution or down to produce a more sparse distribution,
      note that performance will deteriorate for high densities.

    :param seed: string to use as source of characters
    :return: a unique palindromic string not previously generated for this seed
    """

    n=len(seed)
    if not n: return

    allseen=set()
    l=1
    for l in xrange(1, MAX_LENGTH):
        hits=0
        misses=0
        seen=set()
        hit_rate=0

        while hit_rate < MAX_HIT_RATE:
            D=deque()
            x=l
            if l % 2:
                i=random.randint(0, n - 1)
                s=seed[i]
                D.append(s)
                x-=1
            while x > 0:
                i=random.randint(0, n - 1)
                s=seed[i]
                D.appendleft(s)
                D.append(s)
                x-=2

            pal=''
            for p in D:
                pal+=p
            if pal in seen:
                hits+=1
            else:
                misses+=1
                seen.add(pal)
                if not pal in allseen:
                    allseen.add(pal)
                    print pal
                    yield pal
            hit_rate = float(hits) / float(hits + misses) * 100
    return

class TestPalindromes(unittest.TestCase):
    def test_palindromes(self):
        NUM_PROBES = 4000
        for seed in ['abc', 'a', 'elephant']:
            responses = set()
            for _, response in itertools.izip(xrange(NUM_PROBES), palindromes(seed)):
                self.assertNotIn(response, responses)
                for i in xrange(-(-len(response)//2)):
                    self.assertEqual(response[i], response[-(i+1)])
                responses.add(response)
