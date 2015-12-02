"""
Implement a 6 sided die with weights on the sides, so that we don't have an even probability
distribution, but it is weighted by a list of weights passed in at construction time.

After a large number of iterations of throwing this die, the results should closely match the desired
distribution.
"""

import time
import random
random.seed(time.time())

class SixSidedWeightedDie(object):
    MULTIPIER=1000.0

    # NOTE: since these are weights on a probability distribution, these should sum to one, and the incoming array
    # should be of length 6. You should throw if either of these preconditions is false
    def __init__(self, weights):
        super(SixSidedWeightedDie, self).__init__()
        # Validate input
        if len(weights) != 6:
            raise RuntimeError("weights argument should be a list of length 6")
        for weight in weights:
            if weight < 1.0/self.MULTIPIER:
                raise RuntimeError("minimal allowed weight is " + str(1/self.MULTIPIER))
        sum_weights = sum(weights)
        if round(sum_weights, 2) != 1.00:
            raise RuntimeError("weights must sum to 1")

        # divide a range of 1 to MULTIPIER based on the weights
        self._ranges=[0.0] * 6
        self._ranges[0]=weights[0] * self.MULTIPIER
        for i in xrange(1, 6):
            self._ranges[i]= self._ranges[i-1] + weights[i] * self.MULTIPIER;

    # Throw the die: this should produce a value in [1,6]
    def throw_die(self):
        x = random.randint(1, self.MULTIPIER)
        for i in xrange(6):
            if x <= self._ranges[i]: return i+1
