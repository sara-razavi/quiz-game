# Name: Sara Razavi
# Student ID: 970050118
# Project date: december 3, 2019
# Focus: while loops, if/elif, input(), variables, lists

print("================================")
print("        MINI QUIZ GAME")
print("================================")
print("Answer the questions and see your score.\n")

questions = [
    "What does CPU stand for?",
    "Which language is mainly used for web page structure?",
    "What is 5 * 6?",
    "Which one is a Python collection?",
    "What does len() return?"
]

answers = [
    "central processing unit",
    "html",
    "30",
    "list",
    "length"
]

score = 0
question_number = 0

while question_number < len(questions):
    print("Question", question_number + 1)
    print(questions[question_number])

    user_answer = input("Your answer: ").lower().strip()

    if user_answer == answers[question_number]:
        print("Correct!\n")
        score += 1
    else:
        print("Not quite.")
        print("The answer was:", answers[question_number])
        print()

    question_number += 1

print("--------------------------------")
print("Quiz finished!")
print("Your score:", score, "/", len(questions))

if score == len(questions):
    print("Perfect score!")
elif score >= 3:
    print("Good job.")
else:
    print("You need a little more practice.")

print("--------------------------------")

# extra loop.
again = input("Do you want to play again? (y/n): ").lower()

while again != "y" and again != "n":
    print("Please enter y or n.")
    again = input("Play again? (y/n): ").lower()

if again == "y":
    print("Restart the program to play again.")
else:
    print("Bye!")
