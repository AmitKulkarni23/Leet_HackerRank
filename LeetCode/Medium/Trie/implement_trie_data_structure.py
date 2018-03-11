class TrieNode:
    """
    Helper class which actually creates a trie node
    """
    def __init__(self):
        # Creating a list with 26 keys
        # This is because it is mentioned in the problem that there
        # are only 26 letters in the laphabet
        self.children = [None] * 26

        # boolean flag to mark the end of the word
        self.is_end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    
    def char_to_index(self, ch):
        """
        Given a character c, return its absolute
        index in the children list present in the
        TrieNode
        """
        return ord(ch)-ord('a')
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
       
        # Start from the root
        node = self.root
        
        for level in range(len(word)):
            # Get the relative index of each character
            # in the word
            index = self.char_to_index(word[level])
            
            if not node.children[index]:
                # There is no TrieNode present here
                # Create one
                node.children[index] = TrieNode()
            
            # Navigate to this particular index
            node = node.children[index]
            
            
        # Mark the end of the word after insertion
        node.is_end = True
            
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        # Start with teh root node
        node = self.root
        
        # Then check if there is Trie node present
        # for each character
        
        for item in range(len(word)):
            index = self.char_to_index(word[item])
            
            if not node.children[index]:
                # Not present, return False
                return False
            
            # Navigate to the next link
            node = node.children[index]
        
        # Finally return if we have reached the end of the node
        return node.is_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        # Similar to searching for a word in the trie data structure
        # But we do not need to worry about whether we have reached the
        # end of the node
        
        # Start with root
        node = self.root
        
        # Then check if there is a trie node present for each character
        for i in range(len(prefix)):
            index = self.char_to_index(prefix[i])
            
            if not node.children[index]:
                return False
            
            node = node.children[index]
        
        return True
        
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)