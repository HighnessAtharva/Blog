def minJumps(arr, n):
    # The number of jumps needed to reach the starting index is 0
    if (n <= 1):
      return 0
    
    # Return -1 if not possible to jump
    if (arr[0] == 0):
      return -1
    
    # initialization
    # stores all time the maximal reachable index in the array
    maxReach = arr[0] 
    # stores the amount of steps we can still take
    step = arr[0]
    # stores the amount of jumps necessary to reach that maximal reachable position
    jump = 1
    
    # Start traversing array
    
    for start in range(1, n):
        # Check if we have reached the end of the array
        if (start == n-1):
          return jump
        
        # updating maxReach
        maxReach = max(maxReach, start + arr[start])
        
        # we use a step to get to the current index
        step -= 1;
        
        # If no further steps left
        if (step == 0):
          # we must have used a jump
            jump += 1
           
          # Check if the current index / position or lesser index
          # is the maximum reach point from the previous indexes
            if(start >= maxReach):
                return -1
        
          # re-initialize the steps to the amount
          # of steps to reach maxReach from position i.
            step = maxReach - start;
    return -1
    
 
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)
print("Minimum number of jumps to reach end is: ", minJumps(arr, size))
