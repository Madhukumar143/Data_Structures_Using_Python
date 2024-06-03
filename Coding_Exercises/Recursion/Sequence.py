# input -> n(for ex 5)
# output -> 5432112345
# base(exit) case n=0 retrun
# Recurring case seq(n-1) close to base case
# pseudocode
'''
seq(n):
 if n=0  return
 else print(n) seq(n-1) print(n)
'''


def seq(n):
    if n == 0:
        return
    else:
        print(n, end="")
        seq(n - 1)
        print(n, end="")
seq(6)


