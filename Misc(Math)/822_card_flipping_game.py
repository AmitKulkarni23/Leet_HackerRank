def flipgame(fronts, backs):
    """
    :type fronts: List[int]
    :type backs: List[int]
    :rtype: int
    """

    # Credits -> https://leetcode.com/problems/card-flipping-game/solution/
    if fronts == backs:
    # Both the lists are equal
    # Then no number is good
      return 0

    f_len = len(fronts)
    b_len = len(backs)

    same = {x for i, x in enumerate(fronts) if x == backs[i]}

    min_num = 9999

    for i in itertools.chain(fronts, backs):
        if i not in same:
            min_num = min(min_num, i)

    return min_num % 9999


fronts = [1,1]
backs = [2, 1]

print(flipgame(fronts, backs))
