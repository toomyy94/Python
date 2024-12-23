import sys

def f(n):
    if n < 0:
        result = []
    elif n == 0:
        result = [1]
    elif n == 1:
        result = [1, 1]
    else:
        result = f ( n - 1 )
        result.append(result[n-1] + result[n-2])

    return result

if len(sys.argv) == 2 and sys.argv[1].isdigit():
    print (f (int(sys.argv[1])))
else:
    print("Usage " + sys.argv[0] + " number")
