n = float(input("n?"))
k = float(input("k?"))

def arranjo(n, k):
    if k == 0:
        return 1
    else:
        return (n * arranjo((n-1), (k-1)))


print(arranjo(n, k))
