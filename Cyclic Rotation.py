# Cyclic Rotation

def rotate(A, K):
    B = [0] * len(A)                  #Creates a list B with length of A and all values are 0
    
    while K >= len(A):                #If K is greater than or equal to length of A we redefine it to be an equivalent but smaller K value (K=1 is the same as K = len(A) + 1)
        K = K - len(A)                #This is doen by repeatedly subtracting length until its less than length (as small as possible)
    
    for i in range(0, len(A)):
        C = A[i]                   #Sets C which is the holder variable to the current element in A

        if K + i >= len(A):        #Writes C onto B by writing on the index of B shifted left by K, and this condition is for when it needs to be wrapped around back to the start
            B[(K+i)-len(A)] = C    
        else:                      #Same as above but for when a wrap around is not needed
            B[K+i] = C

    return B
