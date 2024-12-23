def estimate_pi(terms):
    result = 0.0
    for n in range(terms):
        result += (-1.0)**n/(2.0*n+1.0)
    return 4*result


print(estimate_pi(100))
print(estimate_pi(1000))