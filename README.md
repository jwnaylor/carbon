# Exercises-Python
==========================

NOTE: DO NOT FORK THIS REPO ON GITHUB.

==========================

Testing materials for candidates

* Problem 1 - Weighted Die :

Implement a 6 sided die with weights on the sides, so that we don't have an even probability distribution, but it is weighted by a list of weights passed in at construction time.  After 100k iterations of throwing this die, the results should closely match the desired distribution, and this should be reproducible in the unit test. The source to extend is in `six_sided_dice.py`.
To run unittest:

`python -m unittest test_weighted_dice`

* Problem 2 - palindrome generator

Write a generator which non-repetitively produces palindromes (strings which read the same reversed) from a given string of characters. By non-repetitively, we mean you can guarantee that any produced value was never produced before. Bonus points for a solution that first produces all 1 letter palindromes, then 2 letter ones, then ... NOTE: if given 'abc', then 'a', 'aa', 'aba', etc are all legal results (i.e., you can repeat the input chars just not the result).

