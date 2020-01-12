# https://leetcode.com/discuss/interview-question/460127/
import re
import heapq
def top_buzz_words(num_toys, top_toys, toys, num_quotes, quotes):
    # Time: O(N * M)
    # Where N -> Total number of quotes
    # M is the max number of words in a quote
    # (Heap construction - O(T) where T is the total number of toys)
    # (Heappop oiperation K log T -> where K is the number of top toys)

    # Space Complexit -> O(T)

    if not toys or not quotes or top_toys == 0:
        return []

    freq_quote_dict = {} # Dictionary of the form
    # {toy : (total_number_of_occurrences, total_number_of_quotes_this_toy_occurs_in)}
    for t in toys:
        freq_quote_dict[t] = (0, 0)

    for q in quotes:
        is_buzzword_updated = {t : False for t in toys} # We want to update the quote count
        # for a particular buzzword/toy only once per quote

        # Clean the quote
        for w in q.lower().split():
            w = re.sub('[^a-z]', '', w) # Replace non a-z characters by ""

            if freq_quote_dict.get(w):
                # This word is a buzzword/toy
                curr_freq, curr_qoute_count = freq_quote_dict[w][0], freq_quote_dict[w][1]

                if not is_buzzword_updated[w]:
                    # This word occurs for the first time in this quote
                    curr_qoute_count += 1
                    is_buzzword_updated[w] = True

                freq_quote_dict[w] = (curr_freq + 1, curr_qoute_count)

    # Initially all toys were initialzied with (0, 0)
    # Remove all toys which do not appear in any of the quotes
    for t in toys:
        if freq_quote_dict[t][0] == 0:
            del freq_quote_dict[t]

    if top_toys > num_toys:
        return [toy for toy in freq_quote_dict]  # Corner Case / Requirement

    # Use heap.
    # Create a min-heap
    # Order by total freq, total quotes the toy appears in, then lexicographically the toy itself

    buzzword_heap = []

    for t in freq_quote_dict:
        freq, quote_count = freq_quote_dict[t][0], freq_quote_dict[t][1]
        buzzword_heap.append((-1 * freq, -1 * quote_count, t))

    heapq.heapify(buzzword_heap)

    result = []
    # Return the requeired number of top toys
    for i in range(top_toys):
        toy = heapq.heappop(buzzword_heap)[2]
        result.append(toy)

        if not buzzword_heap:
            # handling corner case where number of occurences of toys <
            # number of top request toys
            break

    return result


# Example:

num_toys = 6
top_toys = 2
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
num_quotes = 6
quotes = [
"Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
"The new Elmo dolls are super high quality",
"Expect the Elsa dolls to be very popular this year, Elsa!",
"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
"For parents of older kids, look into buying them a drone",
"Warcraft is slowly rising in popularity ahead of the holiday season"
]

print(top_buzz_words(num_toys=num_toys, top_toys=top_toys, toys=toys, num_quotes=num_quotes, quotes=quotes))
