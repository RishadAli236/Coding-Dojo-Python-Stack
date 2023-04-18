# Create an empty dictionary

# come up with 5 vocabulary words as a group. It can be related to python or something separate

# Create a dictionary with the vocabulary words as keys and a nested dictionary with the definition and key 

# Make a list out of the values and pick a random question

# Use the built in input() function to get user input for the answer

# Compare the input to the key and print correct if its right, and incorrect if its wrong. 

# Wrap this all in a function called flash_cards(dictionary)

# Example
import random

programming_languages = {
    "python": {
        "definition": "A standardized interpreted programming language universally used in web development, software, data science and machine learning",
        "key": "python"
    },
    "html": {
        "definition": "The standard markup language for Web pages",
        "key": "html"
    },
    "javascript": {
        "definition": "The programming language of the Web.",
        "key": "javascript"
    },
    "css": {
        "definition": "the language we use to style an HTML document",
        "key": "css"
    },
    "sql": {
        "definition": " is a standard language for storing, manipulating and retrieving data in databases",
        "key": "sql"
    }
}

# # Using a for loop
# list_of_questions = []
# for dictionary in programming_languages.values():
#         list_of_questions.append(dictionary["definition"])
# while True:
#     random_question = random.choice(list_of_questions)
#     user_input = input(random_question + "\n")
#     if user_input == "stop":
#         break
#     elif random_question == programming_languages[user_input]["definition"]:
#         print("Way to go!")
#     else:
#         print("Better luck next time!")





# Without for loop
dictionary_list = list(programming_languages.values()) # returns a list of the nested dictionaries
while(True):
    random_dictionary = random.choice(dictionary_list) # pick a random dictionary
    random_definition = random_dictionary["definition"] # return the definition value of the random dictionary
    user_input= input(random_definition + "\n")
    if user_input == "stop":
        break
    elif(user_input == random_dictionary["key"] ):
        print("Way to go!")
    else:
        print("Better luck next time")
    print("\n")



