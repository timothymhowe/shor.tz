import functools

class WordBreaker(object):
    from typing import List

    def word_break(self, s: str, word_dict: List[str]) ->bool:
        """

        :param s: the string being broken up into words
        :param word_dict: the list of possible words to break up in the dictionary
        :return:
        """
        trie = Trie()  # create empty Trie

        # O(length of word_dict * length of each word)
        for word in word_dict:  # for each word in dictionary, build trie one at a time
            trie.add(word)

        print(trie.root.children)
        return trie.find(s)

    # def word_break(self, s: str, wordDict: List[str]) -> List[str]:
    #     """ O(N)TS """
    #
    #     # @functools.cache
    #     def fn(i):
    #         return any(1 for j in range(i + 1, len(s)) if s[i:j] in d and fn(j)) if s[i:] not in d else True
    #
    #     d = set(wordDict)
    #     return fn(0)


class TrieNode(object):
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.terminates = False

class Trie:

    # Initializing the Trie class
    def __init__(self):
        self.root = TrieNode(None)
        self.memo = {} # creating a dict for memoization aka the dynamic programming part of this solution

    def add(self, word):

        root = self.root
        # iterate through each character in the word
        for char in word:

            if char not in root.children:   # if the character does not exist in the children
                root.children[char] = TrieNode(char)
            # moving to the children
            root = root.children[char]

        # set boolean to mark the end of the word.  This is how the word break is actually executed.
        root.terminates = True

    def find(self, s):
        root = self.root
        for i, char in enumerate(s):
            if char not in root.children:  # if the character is not in the children of the root word
                return False  # then retuurn false

            if root.children[char].terminates: # if the char is terminal:
                if s[i+1] not in self.memo: # if the remainder is has not been memoized before:
                    self.memo[s[i+1:]] = self.find(s[i+1]) # add the remainder to the dictionary
                if self.memo[s[i+1:]]: # if the remainder has been memoized before
                    return True # return true, because it is already part of the dictionary
            root = root.children[char] # continye down the branch
        return root.terminates  # return True if the last character of the input is marked as a leaf node, else False



def memo (f):
    "Memoize function f, with hashable arguments"
    f_cache = {}

    def fmemo(*args):
        if args not in f_cache:
            f_cache[args] = f(*args)
        return f_cache[args]
    fmemo.cache = f_cache
    return fmemo


def splits(text, start=0, L=20):
    "Return a list of all (first, rest) pairs; start <= len(first) <= L."
    return [(text[:i], text[i:])
            for i in range(start, min(len(text), L)+1)]

@memo
def segment(text):
    "Return a list of words that is the most probable segmentation of text."
    if not text:
        return []
    else:
        candidates = ([first] + segment(rest)
                      for (first, rest) in splits(text, 1))
        return max(candidates, key=Pwords)