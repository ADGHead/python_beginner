def add_indexes(x, y):
    letters = "ABCDEFGHIJKLOMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    guess = ""
    try:
        for i in x:
            if i.lower() in letters:
                if i.isupper():
                    shifting = letters.index(i)
                    result = letters[shifting + y]
                    result.upper()
                else:
                    shifting = letters.index(i)
                    result = letters[shifting + y]
            guess+=result
        print(guess)
    except IndexError as err:
        print(err)
            
            
try:
    word = input("Please enter a word of your choice: ")
    integer = int(input("Please enter a number of your choice: "))
    print(add_indexes(word,integer))
except ValueError as err:
    print(err)
