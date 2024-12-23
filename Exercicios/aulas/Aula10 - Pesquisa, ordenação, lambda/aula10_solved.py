def ex2(dict):
    return sorted(dict, key = lambda i: len(i), reverse = True)


dict_ex2 = {
    "e": 33406,
    "a": 32088,
    "o": 28598,
    "ola": 285923,
    "oi": 2859232

}

print("Ex2-.")
print(ex2(dict_ex2))
print("-----")

def median(thelist):
    sorted_list = sorted(thelist)
    length = len(sorted_list)
    center = length // 2

    if length == 1:
        return sorted_list[0]

    elif length % 2 == 0:
        return sum(sorted_list[center - 1: center + 1]) / 2.0

    else:
        return sorted_list[center]


print("Ex4-.")
print(median([0,1,2,3,4,5])) # output = 2.5
print("-----")