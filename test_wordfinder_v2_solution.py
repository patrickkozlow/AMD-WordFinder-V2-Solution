import unittest
import wordfinder_v2_solution


class TrieNodeClassTests(unittest.TestCase):
    def setUp(self):
        self.trie = wordfinder_v2_solution.TrieNode()

    def test_add_word1(self):
        trie = wordfinder_v2_solution.TrieNode()
        test = 'test'
        trie.add_word(test)
        for c in test:
            if not trie.isWord:
                self.assertEqual(c, list(trie.children)[0])
            trie = trie.children[c]

    def test_add_words(self):
        trie = wordfinder_v2_solution.TrieNode()
        test = ['test', 'tester', 'taste', 'tet']
        for w in test:
            trie.add_word(w)
        for c in 'tester':
            if not trie.isWord:
                self.assertEqual(c, list(trie.children)[0])
            trie = trie.children[c]


class SolutionTests(unittest.TestCase):
    def test_find_words1(self):
        trie = wordfinder_v2_solution.TrieNode()
        test_words = ['test', 'apple', 'ape', 'abc']
        board = [[2, 2], ['a', 'b'], ['e', 'c']]
        for w in test_words:
            trie.add_word(w)
        res = wordfinder_v2_solution.Solution().find_words(board, test_words)
        self.assertEqual(res, ['1', 'abc'])

    def test_find_words2(self):
        trie = wordfinder_v2_solution.TrieNode()
        test_words = ['a', 'ab', 'abe', 'abba', 'aba']
        board = [[2, 2], ['a', 'b'], ['e', 'c']]
        for w in test_words:
            trie.add_word(w)
        res = wordfinder_v2_solution.Solution().find_words(board, test_words)
        self.assertEqual(res, ['3', 'a', 'ab', 'abe'])


if __name__ == '__main__':
    unittest.main()
