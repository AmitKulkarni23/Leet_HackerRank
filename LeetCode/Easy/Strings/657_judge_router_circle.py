# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
#
# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.
#
# Example 1:
# Input: "UD"
# Output: true
# Example 2:
# Input: "LL"
# Output: false

# Runtime : 141 ms
def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    # Credits : https://leetcode.com/problems/judge-route-circle/solution/
    # Initialize x, y to 0
    x = y = 0

    # Iterate through the string
    for ch in moves:
        if ch == "U":
            y -= 1
        elif ch == "D":
            y += 1
        elif ch == "L":
            x -= 1
        elif ch == "R":
            x += 1

    return x == y == 0

# Runtime : 35 ms
def best_leetcode_sol_judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    return (moves.count('U')==moves.count('D')) and (moves.count('L')==moves.count('R'))
