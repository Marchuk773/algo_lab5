import unittest

from main import naive_search


class AlgorithmTests(unittest.TestCase):
    
    def testAlgorithm(self):
        self.assertEqual(naive_search('ORAORAORAORA', 'oRA', case_insensitive=True), [0, 3, 6, 9])
        self.assertEqual(naive_search('ORAORAORAORA', 'oRA'), [])
        self.assertEqual(naive_search('ABBA', 'BA'), [2])
        self.assertEqual(naive_search('AABAACAADAABAAABAA', 'AABA'), [0, 9, 13])


if __name__ == '__main__':
    unittest.main()
