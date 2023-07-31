# Checker Excercise 2
def checker_2(x):
    num_4 = x[4]
    if len(x) == 8 and x.count(num_4) == 3:
        return True
    else:
        return False

words = [19, 19, 15, 5, 5, 5, 1, 2]

print(checker_2(words))