# The following is a description of the instance of this famous puzzle
# involving n=2 eggs and a building with k=36 floors.
#
# Suppose that we wish to know which stories in a 36-story
# building are safe to drop eggs from, and which will cause the eggs to break on landing

##############################

def egg_drop_recursive(n, k):
    """
    Function that returns the minimum number of trials needed
    to determine what is maximum floor from which an egg can be dropped
    without it breaking

    """
    
