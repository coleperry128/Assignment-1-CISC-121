# Tape Equilibrium

def smlstdiff(A):
    mindiff = 0                          #Create a variable to hold the smallest difference
    
    for i in range(1, len(A)-1):         #Repeat for every possible seperation point (what's called P in the question)
        diff = sum(A[:i]) - sum(A[i:])   #Calculates the difference between all the values of the array up to the seperation point, minus the values after it

        if diff < 0:                     #If this difference is negative make it positive because we need the absolute value
            diff = diff * -1

        if diff < mindiff or i == 1:     #If this difference is less than the held minimum distance than make this ith difference the new minimum difference
            mindiff = diff

    return mindiff
