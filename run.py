# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
print("Welcome to my SMITE quiz game. Answer the questions as they appear.")

class Question:
    """
    function to initialise a question with
    multiple choices
    """
    def __init__(self, question_text, answer, multiple_choice_options=None):
        self.question_text = question_text
        self.answer = answer
        self.multiple_choice_options = multiple_choice_options
    
    def __repr__(self):
        return '{'+ self.question_text +','+ self.answer +', '+ str(self.multiple_choice_options) +'}'


quizQuestions = [
    Question("Q1. Who is the God of Lightning from Greek Mythology", "a", ["(a) Zeus" , "(b) Vulcan", "(c) Apollo", "(d) Bacchus"]),
    Question("Q2. How many Pantheons are there currently in SMITE?", "d", ["(a) 10" , "(b) 12", "(c) 14", "(d) 16"]),
    Question("Q3. What class does Agni belong to?", "c", ["(a) Warrior" , "(b) Assassin", "(c) Mage", "(d) Guardian"])
    ]

for question in quizQuestions:
    if (question.multiple_choice_options != None):
        print(f"{question.question_text}?")
        for option in question.multiple_choice_options:
            print(option)
        userInput = input()
    else:
        print(f"{question.question_text}?")
        userInput = input()
    if (userInput.lower() == question.answer.lower()):
        print("Yes! Correct answer.")
    else:
        print(f"Sorry that was an incorrect answer. Answer is {question.answer}")