# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
print("Welcome to my SMITE quiz game. Answer the questions as they appear.")

class Question:
    def __init__(self, questionText, answer, multipleChoiceOptions=None):
        self.questionText = questionText
        self.answer = answer
        self.multipleChoiceOptions = multipleChoiceOptions
    
    def __repr__(self):
        return '{'+ self.questionText +','+ self.answer +', '+ str(self.multipleChoiceOptions) +'}'


quizQuestions = [
    Question("Q1. Who is the God of Lightning from Greek Mythology", "a", ["(a) Zeus" , "(b) Vulcan", "(c) Apollo", "(d) Bacchus"]),
    Question("Q2. How many Pantheons are there currently in SMITE?", "d", ["(a) 10" , "(b) 12", "(c) 14", "(d) 16"]),
    Question("Q3. What class does Agni belong to?", "c", ["(a) Warrior" , "(b) Assassin", "(c) Mage", "(d) Guardian"])
    ]

for question in quizQuestions:
    if(question.multipleChoiceOptions != None):
        print(f"{question.questionText}?")
        for option in question.multipleChoiceOptions:
            print(option)
        userInput = input()
    else:
        print(f"{question.questionText}?")
        userInput = input()
    if(userInput.lower() == question.answer.lower()):
        print("Yes! Correct answer.")
    else:
        print(f"Sorry that was an incorrect answer. Answer is {question.answer}")