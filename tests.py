import unittest

from main import naive_search
from utils import read_from_file


class AlgorithmTests(unittest.TestCase):
    
    def testAlgorithm(self):
        text, query = read_from_file('files/file1.in')
        self.assertEqual(naive_search(text, query, case_insensitive=True), [0, 3, 6, 9])
        self.assertEqual(naive_search(text, query), [])
        text, query = read_from_file('files/file2.in')
        self.assertEqual(naive_search(text, query), [2, 5])
        text, query = read_from_file('files/file3.in')
        self.assertEqual(naive_search(text, query), [0, 9, 13])


if __name__ == '__main__':
    unittest.main()
