secret_word = "giraffe"
guess = ""
limit = 3
guess_count = 0
finished_guesses = False

while guess != secret_word and finished_guesses == False:
    if guess_count < limit:
        guess = input("Please Input The secret Word")
    else:
        finished_guesses = True
    guess_count +=1

if finished_guesses == True:
    print("You loose!")
else:
    print("You Win")



