# Given a chessboard, how would you find whether the king is
# threatened by the queen.

# Input: Two pieces on the chessboard
# kx, ky, qx, qy

# Output: True or False

# Case: There are no more pieces on the chessboard

def check_mate(kx. ky, qx, qy):
    return kx == qx or ky == qy or abs(kx - qx) == abs(ky - qy)
