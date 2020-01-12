# https://leetcode.com/problems/search-suggestions-system/

"""
Given an array of strings products and a string searchWord. We want to design a
system that suggests at most three product names from products after each character
of searchWord is typed. Suggested products should have common prefix with the searchWord.
If there are more than three products with a common prefix return the three
lexicographically minimums products.

Return list of lists of the suggested products after each character of
searchWord is typed.



Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]


Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
"""

def suggestedProducts(products, searchWord):
    """
    :type products: List[str]
    :type searchWord: str
    :rtype: List[List[str]]
    """

    # Approach 1:
    answer = []
    # Sort the products array -> O(n * log n)  where n is the number of products
    products.sort()

    for idx, c in enumerate(searchWord):
        products = [p for p in products if len(p) > idx and p[idx] == c]
        answer.append(products[:3]) # The top 3 results

    return answer

    # Approach 2: Trie based approach
