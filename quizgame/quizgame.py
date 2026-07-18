print("Welcome to my quiz game!")

playing = input("Do you want to play a game? ").lower()

if playing != "yes":
    quit()

print("Okay, let's play!")
score = 0
total_questions = 0


def ask(question, correct_answer):
    global score, total_questions
    total_questions += 1
    answer = input(question + " ").strip().lower()
    if answer == correct_answer.lower():
        print("That's correct!")
        score += 1
    else:
        print("Incorrect!")
        print(f"The correct answer was: {correct_answer}")


# Questions
ask("What does CPU stand for?", "Central Processing Unit")
ask("What does ISP stand for?", "Internet Service Provider")
ask("What does SMTP stand for?", "Simple Mail Transfer Protocol")
ask("What does WWW stand for?", "World Wide Web")
ask("What does DNS stand for?", "Domain Name System")
ask("What does RAM stand for?", "Random Access Memory")
ask("What does GPU stand for?", "Graphics Processing Unit")
ask("What does URL stand for?", "Uniform Resource Locator")
ask("What does HTML stand for?", "HyperText Markup Language")
ask("What does IP stand for?", "Internet EProtocol")
ask("What dose HTTP stand for", "Hyper Text Transfer Protocol")

print("\nYou got " + str(score) +
      " questions right out of " + str(total_questions))

percentage = (score / total_questions) * 100
print(f"Your score percentage is: {percentage:.2f}%")

if percentage == 100:
    print("Excellent! Perfect score!")
elif percentage >= 70:
    print("Great job!")
elif percentage >= 40:
    print("Not bad, keep practicing!")
else:
    print("You need more practice, but you can do it!")
