# input = n -> int -> 5
# output = n! (120)

def fact(n):
    if n == 1 :
        return 1
    else :
        return (fact(n-1) *n)

a = fact(5)
print(a)