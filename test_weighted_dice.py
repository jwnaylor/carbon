import unittest
from six_sided_dice import SixSidedWeightedDie

class TestWeightedDice(unittest.TestCase):

    def test_weights(self):
        DELTA = 0.0035
        NUM_THROWS = 100000

        weights = [.05, .10, .15, .2, .2, .3]
        the_die = SixSidedWeightedDie(weights)
        counts = [0 for _ in xrange(6)]

        for _ in xrange(NUM_THROWS):
            counts[the_die.throw_die() - 1] += 1

        for i in xrange(6):
            self.assertAlmostEqual(float(counts[i])/NUM_THROWS, weights[i], delta=DELTA) 
