
import datetime
import random

name = input("Enter your name: ")
userAge = input("Enter your age: ")
favoriteColor = input("What is your favorite color? ")
favoriteLanguage = input("What is your favorite programming language? ")
print("\nAssalamoyalaikum", name)

#Chat History File
historyFile = "chat_history.txt"

# Greeting System
presentHour = int(datetime.datetime.now().strftime("%I"))
presentPeriod = datetime.datetime.now().strftime("%p")

if 5 <= presentHour < 12 and presentPeriod == "AM":
    print("Good morning,", name)
elif (presentHour == 12 or presentHour < 5) and presentPeriod == "PM":
    print("Good afternoon,", name)
elif 5 <= presentHour < 9 and presentPeriod == "PM":
    print("Good evening,", name)


print("\nWelcome to Your ChatBot!")
print("Type 'bye' to exit.")

responses = {
    "hello": "Hi! How can I help you?",
    "how are you": "I am doing great! Thanks for asking.",
    "who are you": "I am SmartBot, your personal assistant.",
    "motivate me": "Believe in yourself. You can achieve great things!",
    "thank you": "You are most welcome!",
    "your name": "My name is SmartBot.",
    "good morning": "Good morning! Have a wonderful day!",
    "good night": "Good night! Sweet dreams!",
    "what can you do": "I can tell jokes, share facts, calculate numbers and more!",
    "help me": "Of course! Tell me what you need help with."
}

facts = [
    "Octopuses have three hearts!",
    "A day on Venus is longer than its year!",
    "Sharks existed before trees!",
    "Bananas are botanically classified as berries!",
    "Lightning can be hotter than the surface of the Sun!",
    "Honey can remain edible for thousands of years when properly stored!",
    "The human brain contains billions of neurons!",
    "Some turtles can breathe through specialized tissues near their tails!",
    "A group of flamingos is called a flamboyance!",
    "The Eiffel Tower can become slightly taller during hot weather!"
]


jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? Because it left its Windows open!",
    "Why do Python programmers wear glasses? Because they cannot C!",
    "Why did the developer go broke? Because he used up all his cache!",
    "Why do programmers hate nature? It has too many bugs!",
    "What is a computer's favorite snack? Microchips!",
    "Why did the programmer quit his job? Because he did not get arrays!",
    "What do you call a computer that sings? A-Dell!",
    "Why was the JavaScript developer sad? Because he did not know how to Express himself!",
    "Why did the computer go to the doctor? Because it had a virus!"
]


def calculator(num1, operator, num2):

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return "Cannot divide by zero!"
        return num1 / num2

    else:
        return "Invalid operator!"

# ChatBot Response Function
def getResponseOfBot(userQuestion, name, userAge, favoriteColor, favoriteLanguage):

    userQuestion = userQuestion.lower()

    if "fact" in userQuestion:
        return random.choice(facts)

    if "joke" in userQuestion or "laugh" in userQuestion:
        return random.choice(jokes)

    now = datetime.datetime.now()

    if "date" in userQuestion:
        return "Today's date is " + now.strftime("%d %B %Y")
    elif "day" in userQuestion:
        return "Today is " + now.strftime("%A")
    elif "time" in userQuestion:
        return "Current time is " + now.strftime("%I:%M:%S %p")
    elif "year" in userQuestion:
        return "Current year is " + str(now.year)
    elif "month" in userQuestion:
        return "Current month is " + now.strftime("%B")

    if "lucky number" in userQuestion:
        return "Your lucky number is " + str(random.randint(1, 999))

    elif "random number" in userQuestion:
        return "Your random number is " + str(random.randint(1, 999))

     # Mood Detection
    if "happy" in userQuestion or "joy" in userQuestion:
        return "That's wonderful! Keep smiling!"

    elif "sad" in userQuestion or "upset" in userQuestion:
        return "Don't worry. Better days are ahead!"

    elif "angry" in userQuestion or "mad" in userQuestion:
        return "Take a deep breath and stay calm."

    elif "excited" in userQuestion:
        return "That's awesome! Enjoy your excitement!"

    elif "tired" in userQuestion or "exhausted" in userQuestion:
        return "Take a little rest. You deserve a break."

    elif "bored" in userQuestion:
        return "Let's do something interesting!"

    elif "confused" in userQuestion:
        return "Don't worry. Take it one step at a time!"

    # Simple Calculator
    if "calculate" in userQuestion or "calculator" in userQuestion:

        try:
            numbers = userQuestion.split()

            num1 = float(numbers[1])
            operator = numbers[2]
            num2 = float(numbers[3])

            result = calculator(num1, operator, num2)

            return "Calculation Result: " + str(result)

        except (ValueError, IndexError):
            return "Please write like this: calculate 10 + 20"

    #User Personalization
    if "my name" in userQuestion:
        return f"Your name is {name}."

    elif "my age" in userQuestion:
        return f"You are {userAge} years old."

    elif "my favorite color" in userQuestion:
        return f"Your favorite color is {favoriteColor}."

    elif "my favorite language" in userQuestion:
        return f"Your favorite programming language is {favoriteLanguage}."

    elif "who am i" in userQuestion:
        return f"You are {name}, and you love {favoriteLanguage}!"

    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to tell that yet. I will learn it soon!"


# User Interaction
while True:

    userInput = input("\nAsk your question: ")

    if "bye" in userInput.lower():

        goodbyeMessage = "Goodbye, " + name 

        print("Bot Response:", goodbyeMessage)
        if 9 <= presentHour  and presentPeriod == "PM":
            print("Good Night, Have a Sweet Dream")

        with open(historyFile, "a") as file:
            file.write("User: " + userInput + "\n")
            file.write("Bot: " + goodbyeMessage + "\n")
            file.write("-------------------------\n")

        break

    reply = getResponseOfBot(
        userInput,
        name,
        userAge,
        favoriteColor,
        favoriteLanguage
    )

    print("Bot Response:", reply)

    #Save Chat History
    with open(historyFile, "a") as file:

        file.write("User: " + userInput + "\n")
        file.write("Bot: " + reply + "\n")
        file.write("-------------------------\n")
