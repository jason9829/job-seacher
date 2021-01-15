

# Desc: Determine when to skip the iterations for JobStreet (first and second object are the same so second object
#        need to be skipped and the link in second object is incorrect.)
# Param: Current iteration
# Retval: Number to increment and decrement to skip the second object
def getIterationValue(current):
    if current == 0:
        return 2
    else:
        return 1