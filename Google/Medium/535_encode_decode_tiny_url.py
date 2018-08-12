# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl
# and it returns a short URL such as http://tinyurl.com/4e9iAk.
#
# Design the encode and decode methods for the TinyURL service.
# There is no restriction on how your encode/decode algorithm should work.
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# Note: Checkout leetcode article -> https://leetcode.com/problems/encode-and-decode-tinyurl/solution/

import random
class Codec:
    def __init__(self):
        self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.my_map = {}
        self.key = self.get_rand()

    def get_rand(self):
        """
        Helper function
        """
        ret_str = ""
        for i in range(6):
            ret_str += self.alphabet[random.randint(0, 61)]

        return ret_str

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        while self.key in self.my_map:
            self.key = self.get_rand()

        self.my_map[self.key] = longUrl
        return "http://tinyurl.com/" + self.key


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.my_map[shortUrl.replace("http://tinyurl.com/", "")]


# Your Codec object will be instantiated and called as such:
codec = Codec()
url = "www.google.com"
print(codec.decode(codec.encode(url)))


# The number of URLs that can be encoded is quite large in this case, nearly of the order (10+26*2)^6
# The length of the encoded URLs is fixed to 6 units, which is a significant reduction for very large URLs.
# The performance of this scheme is quite good, due to a very less probability of repeated same codes generated.
# We can increase the number of encodings possible as well, by increasing the length of the encoded strings.
# Thus, there exists a tradeoff between the length of the code and the number of encodings possible.
# Predicting the encoding isn't possible in this scheme since random numbers are used.
