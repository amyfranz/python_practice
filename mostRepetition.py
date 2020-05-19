string = "this is a some words and it is my test"


def highest_value(string):
    string = string.replace(" ", "").lower()
    dict = {}
    for item in range(len(string)):
        dict[string[item]] = dict.get(string[item], 0) + 1
    x = sorted(dict, key=(lambda key: dict[key]), reverse=True)
    return x[0]


print(highest_value(string))
