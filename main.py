#user information

print("hello and welcome to (game v2) , in this game you will be answering a series of questions to help inprove your knowledge of global warming ")

print (" ")

name = input ("What is your name? ")
print ("Hello " + name)
print(" ")

# tutorial 

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")

show_instructions = yes_no("Have you played the "
                           "game before? ")
print("You chose {}".format(show_instructions))

# rounds start

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "is the ice melting in the artic?: ": "A",
 "why is the ice melting in the artic?: ": "B",
 "is it effecting the animals that live there?: ": "C",
 "are there any ways we could fix this issue?: ": "A"
}

options = [["A. yes", "B. no", "C. maybe", "D. sometimes"],
          ["A. because of trees", "B. because of humans", "C. because of sharks", "D. because of penguins"],
          ["A. no", "B. sometimes", "C. yes", "D. only on weekends"],
          ["A. yes","B. no", "C. sometimes", "D. maybe"]]

new_game()

while play_again():
    new_game()

# completed game 