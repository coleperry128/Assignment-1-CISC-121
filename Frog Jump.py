# Frog Jump

def minjumps(X, Y, D):
    jumps = 0                 #Record the number of jumps so far
    while X < Y:              #Loop until frog is at or past the point Y
        jumps = jumps + 1     #Counts jumps as frog moves forward by increments of D
        X = X + D
    return jumps              #Once the frog reaches the position Y, the final value of the number of jumps will be returned as the solution
