"""
This is a solution for the wordfinder_v2 problem

This solution uses a trie data structure along with a dfs search to find the number of english words in a NxN grid.
Assuming englishwords.txt is constant: Time complexity is O(board rows * cols)
"""

# Import functions to input data
from import_data import create_list
from import_data import create_grid


# TrieNode provides utility functions to build nodes for a trie data structure
class TrieNode:
    def __init__(self):
        """
        Constructor to used to create trie nodes
        """
        self.children = {}  # Dictionary containing where key:character, value:child node
        self.isWord = False  # Marking the end of a word

    def add_word(self, word: str) -> None:
        """
        add_word adds nodes to the trie data structure to make complete words

        :param word: A string representing an english word
        :return:
        """

        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True  # Mark the end of the word


# Solution provides the methods/functions and code necessary to solve the problem
class Solution:
    def find_words(self, board: list[list[str]], all_words: list[str]) -> list[str]:
        """
        find_words takes the board and words and uses a trie data structure with dfs to find which words exist in the
        board

        :param board: A matrix of lowercase characters
        :param all_words: A list of english words
        :return: A list containing all possible words and the number of words
        """
        root = TrieNode()   # define the root (head) of the Trie
        for w in all_words:
            root.add_word(w)  # populating trie with words from list of all words

        # Get dimensions of board
        size = board.pop(0)  # remove NxN info from board and use to set rows/cols
        size = list(map(int, size))
        rows, cols = size[0], size[1]
        res, visit = set(), set()  # to prevent returning duplicates

        def dfs(r: int, c: int, node: TrieNode, word: str):
            """
            dfs performs a depth first search to scan each cell around the current cell to see if the next
            character/node exists for the word.

            :param r: int coordinates for current row
            :param c: int coordinates for current column
            :param node: current node in the Trie
            :param word: current english word
            :return:
            """

            # Exit condition
            if (r < 0 or c < 0 or
                    r == rows or c == cols or
                    (r, c) in visit or
                    board[r][c] not in node.children):
                return

            # If a character is found add it to visited and update node/word
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:  # check if end of word has been reached
                res.add(word)

            # Recursive check for all positions around current cell
            for x, y in [[-1, -1], [-1, 0], [-1, 1],
                         [0, -1], [0, 1],
                         [1, -1], [1, 0], [1, 1]]:
                dfs(r + x, c + y, node, word)

            visit.remove((r, c))  # remove visited values before returning

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        result_list = list(res)  # Convert set to list
        num_words = str(len(result_list))  # Count number of words
        result_list.insert(0, num_words)  # Insert to beginning of list
        return sorted(result_list)


# Main Code
if __name__ == '__main__':
    words = create_list('wordfinder_v2/englishwords.txt')
    grid = create_grid('wordfinder_v2/grid.txt')
    result = Solution().find_words(grid, words)
    for elem in result:
        print(elem)
