#Checker Excercise
def checker(x):
    if x.count(19) >= 2 and x.count(5) >= 3:
        return True
    else:
        return False

words = [19, 15, 15, 5, 3, 3, 5, 2]

print(checker(words))