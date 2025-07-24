# importing random module
import random

# Creating subjects

subjects = [
    "The government",
    "Shahrukh Khan",
    "Nirmala Sitharaman",
    "a Mumbai Cat",
    "a Dog in Delhi"
    "a animal rights activist",
    "a famous chef"
]

# Creating actions

actions = ["is planning to",
           "has announced that it will",
           "is considering",
           "has decided to",
           "is expected to"
           "is rumored to be",
           "is set to",
           "is likely to",
           "is rumored to be planning to"
           ]

# Creating Objects

objects = [
    " at Red Fort",
    " in Mumbai Local Train", 
    "a plate of Samosa", 
    "inside parliament",
    "in a local market",
    "in a restaurant"
]

# using while loop to generate fake news

while True:
    # generating random subjects, action, and objects
    subject = random.choice(subjects)
    action = random.choice(actions)
    object = random.choice(objects)

    # taking user input to continue or stop
    user_input = input(f"Do you want to generate fake news? (yes/no): ").strip().lower() # strip removes extra spaces and lower convert the input to lowercase.
    if user_input == "yes":
        print(f"BREAKING NEWS: {subject} {action} {object}")
    
    elif user_input == 'no':
        print("Thank you for using the Fake News Generator!")
        break
