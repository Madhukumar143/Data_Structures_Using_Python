"""Coding Exercise: Josephus problem
There are n friends that are playing a game. 
The friends are sitting in a circle and are numbered from 1 to n in clockwise order.
More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and
moving clockwise from the nth friend brings you to the 1st friend.The rules of the game are as follows:
Start at the 1st friend.Count the next k friends in the clockwise direction including the friend 
you started at.The counting wraps around the circle and may count some friends more than once. 
The last friend you counted leaves the circle and loses the game. If there is still more than one friend 
in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just
lost and repeat. Else, the last friend in the circle wins the game. Given the number of friends, n, 
and an integer k,return the winner of the game."""

def findTheWinner(n, k):

    #Using iteration
    def win(n,k):
        v=0
        for i in range(2,n+1):
            v = (v+k)%i
        return v+1
    return win(n,k)
    
    """ 
    using recursion method 1
    def win(n,k):
        if n==1:
            return 0
        else:
            return (win(n-1,k)+k)%n
    return win(n,k)+1

    using recursion method 2
    arr = [i+1 for i in range(n)]
    def win(arr,start):
        if len(arr)==1:
            return arr[0]
        else:
            length = len(arr)
            index_to_remove = (start+k-1) % length
            del arr[index_to_remove]
            print(arr)
            return win(arr,index_to_remove)
    return win(arr,0)
    """
    
print(findTheWinner(8,5))