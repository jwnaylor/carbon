import unittest

def palindromes(seed):
    pass  # TODO implement


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
