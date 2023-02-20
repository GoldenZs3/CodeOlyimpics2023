# Enter your code here. Read input from STDIN. Print output to STDOUT
def shuffle(A, L, R):
    if R == L + 1:
        A[L], A[R] = A[R], A[L]
        return
    shuffle(A, L, R-1)
    shuffle(A, L+1, R)

T = int(input())
for _ in range(T):
    n,k = input().split()
    n=int(n)
    k=int(k)
    A = list(range(1, n+1))
    shuffle(A, 0, n-1)
    print(A[k-1])