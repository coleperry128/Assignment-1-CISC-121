# PermMissingElem

def missing(A):
    min = 100001                    #Start by setting min to the greates possible value of any element in the array
    for i in range(0, len(A)):      #Loop so that i is every index in A, and compare every value with the current min, changing the minimum value if the next element is smaller             
        if A[i] == 1:    #Here just stop and set the min to 1 if an entry = 1 is found because that's the lowest possible entry.
            min = 1
            break
        elif A[i] < min:
            min = A[i]

    rangeA = list((range(min, (min + len(A) + 1))))  #Create rangeA as the list of all values that should be in the array (range from min to max of A) if it wasn't for the missing number.

    for i in range(0, len(A)):      #Go through all the values of rangeA using each value of A as an index (minus min because index starts at 0)
        rangeA[A[i] - min] = "counted"          #This marks every value of A[i] and marks off its corresponding value in rangeA as counted

    for i in range(0, len(A)):
        if rangeA[i] != "counted":      #There should be only 1 entry in rangeA that isn't marked off, and this is the missing entry.
            return rangeA[i]
