# Odd Occurences in Array:

def oddoccur(A):
    for i in range(0, len(A)):            #A loop that goes through every value of the list
        soln = 0                          #A variable which turns one when an integer's pair has been found
        for n in range(0, len(A)):        #Goes through the list and compares every value to the value with index i
            if A[i] == A[n] and i != n:   #When a pair has been found, stops searching and indicates a pair exists using soln
                soln = 1
                break

        if soln == 0:                     #If no pair has been found for a given entry, returens that value as the odd integer which is the solution
            return A[i]
