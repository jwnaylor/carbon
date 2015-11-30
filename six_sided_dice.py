"""
Implement a 6 sided die with weights on the sides, so that we don't have an even probability
distribution, but it is weighted by a list of weights passed in at construction time.

After a large number of iterations of throwing this die, the results should closely match the desired
distribution.
"""

class SixSidedWeightedDie(object):
    # NOTE: since these are weights on a probability distribution, these should sum to one, and the incoming array
    # should be of length 6. You should throw if either of these preconditions is false
    def __init__(self, weights):
        super(SixSidedWeightedDie, self).__init__()
        # TODO fill in

    # Throw the die: this should produce a value in [1,6]
    def throw_die(self):
        pass # TODO fill in
