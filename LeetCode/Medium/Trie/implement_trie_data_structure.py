"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

"""

class TrieNode:
    """
    Helper class which actually creates a trie node
    """
    def __init__(self):
        # Creating a dictionary
        self.children = {}

        # boolean flag to mark the end of the word
        self.is_end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        # Start from the root node
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                # No TrieNode exists for this character
                # Create one
                node.children[ch] = TrieNode()
            
            # Else if a Trie node already exists, navigate 
            # to that node
            node = node.children[ch]
        
        
        # Mark the end of the node
        node.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        # Start from the root node
        node = self.root
        
        # Iterate through all the characters in the
        # word and check for keys in the children dictionary
        
        for ch in word:
            if ch not in node.children:
                return False
            
            # Now here it is present, therefore
            # move that particular node
            node = node.children[ch]
        
        # For a full word to exist we should have reached
        # the end
        return node.is_end
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        # This is similar to searching for a word
        # Only difference is we do not need to check if end of word has been
        # reached, as we are checking for a prefix only
        
        # Start from the root node
        node = self.root
        
        for ch in prefix:
            if ch not in node.children:
                return False
            
            node = node.children[ch]
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)