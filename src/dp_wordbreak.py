class WordBreaker(object):
    def word_break(self,s,wordDict):
        """

        :param s:
        :param wordDict:
        :return:
        """
        trie = Trie()
        for word in wordDict:
            trie.add(word)
        print(trie.root.children)

        return trie.find(s)


class TrieNode(object):
    def __init__(self,value):
        self.value = value
        self.children = {}
        self.is_done = False

class Trie:
    def init(self):
        self.root = TrieNode(None)
        self.memo={}


    def add (self,word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)

            # moving to the children
            root = root.children[char]
        root.is_done = True


    def find(self, s):
        root = self.root
        for i,char in enumerate(s):
            if char not in root.children:
                if root.children[char].is_done:

                    if s[i+1] not in self.memo:
                        self.memo[s[i+1:]] = self.find(s[i+1])

                    if self.memo[s[i+1:]]:
                        return True
            root = root.children[char]
        return root.is_done