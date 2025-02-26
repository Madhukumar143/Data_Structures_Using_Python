"""
The tower of Hanoi is a famous puzzle where we have three rods and N disks. 
The objective of the puzzle is to move the entire stack to another rod. You are given the number of 
discs N. Initially, these discs are in the rod 1. You need to print all the steps of discs movement 
so that all the discs reach the 3rd rod. Also, you need to find the total moves.
"""

def toh(N, fromm, to, aux):
    #code below
    # sample print statement below
    #print("move disk " + 1 + " from rod " + 1 + " to rod " + 2)
    #in the above statement consider we are moving disk 1 from rod 1 to rod 2
    #remember to return number of moves as well
    count =0
    
    def help(N, fromm, to, aux):
        nonlocal count # because count is not declared globally
        if N==1:
            print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
            count+=1 
            return
        #recursive case 
        help(N-1,fromm,aux,to)
        print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
        count+=1 
        help(N-1,aux,to,fromm)
        
    help(N, fromm, to, aux)
    return count

print(toh(4,1,3,2))
    
    
    

