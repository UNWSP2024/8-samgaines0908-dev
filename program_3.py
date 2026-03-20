# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).

    #Author: Sam Gaines
    #Title: Capital Quiz
    #Date: 3/19/2026
import random

def capital_quiz():
    providence_and_capitals= {
        "Alberta": "Edmonton",
        "British Columbia": "Victoria",
        "Manitoba": "Winnipeg",
        "New Brunswick": "Fredericton",
        "Newfoundland and Labrador": "St. John's",
        "Nova Scotia": "Halifax",
        "Ontario": "Toronto",
        "Prince Edward Island": "Charlottetown",
        "Quebec": "Quebec City",
        "Saskatchewan": "Regina",
        "Northwest Territories": "Yellowknife",
        "Nunavut": "Iqaluit",
        "Yukon": "Whitehorse"
    }

    # This shufflses the questions and doesnt let it repeat. i found that it would repeat alot of questions with only the import random
    provinces_list = list(providence_and_capitals.items())
    random.shuffle(provinces_list)

    correct_answer = 0
    incorrect_answer = 0

    numer_of_questions = 5
    # random providence
    for _ in range(numer_of_questions):
        providence= random.choice(list(providence_and_capitals.keys()))
        capital = providence_and_capitals[providence]
        # asks user the capital of random providence
        user_answer= input(f"What is the capital of {providence}? ")
        # tells the user if its correct
        if user_answer.lower() == capital.lower():
            print(" That's Correct")
            correct_answer+= 1
        else:   # tell user if incorrect
            print(f"Incorrect. The correct answer is {capital}.")
            incorrect_answer += 1

                # Display the results at the end
    print("\nQuiz Over!")
    print(f"You got {correct_answer} questions correct and {incorrect_answer} questions incorrect.")

# Example usage
if __name__ == "__main__":
    capital_quiz()


