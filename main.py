# Show the fun title
print(r"""  ______             __                  ________  __                          __ 
 /      \           |  \                |        \|  \                        |  \
|  $$$$$$\ __    __  \$$ ________        \$$$$$$$$ \$$ ______ ____    ______  | $$
| $$  | $$|  \  |  \|  \|        \         | $$   |  \|      \    \  /      \ | $$
| $$  | $$| $$  | $$| $$ \$$$$$$$$         | $$   | $$| $$$$$$\$$$$\|  $$$$$$\| $$
| $$ _| $$| $$  | $$| $$  /    $$          | $$   | $$| $$ | $$ | $$| $$    $$ \$$
| $$/ \ $$| $$__/ $$| $$ /  $$$$_          | $$   | $$| $$ | $$ | $$| $$$$$$$$ __ 
 \$$ $$ $$ \$$    $$| $$|  $$    \         | $$   | $$| $$ | $$ | $$ \$$     \|  \
  \$$$$$$\  \$$$$$$  \$$ \$$$$$$$$          \$$    \$$ \$$  \$$  \$$  \$$$$$$$ \$$
      \$$$                                                                        
               """)

# Display welcome message and rules of the game
print("Welcome to Quiz Time!")
print("You will answer a few True or False questions. Please ONLY enter the letter T or F when it is your turn to answer. Have fun!")
print()
# Create variable to keep track of correct guesses
exact = 0

# Create variable to keep track of whre we are
note = 0

# Store questions and answers in variables
questions = ("Q1. There are seven continents in the world.", "Q2. Insects have six legs.", "Q3. The Earth is the closest planet to the Sun.", "Q4. Russia is the largest country by area in the world.", "Q5. Ancient Eqyptian civilization was responsible for the pyramids.")
answers = ("T", "T", "F", "T", "T")

numOfQuestions = len(questions)
for num in range(numOfQuestions):

  # Display next question
  print(questions[num])

  # Check user entered only "T" or "F"
  answer = ""

  while(answer != "T" and answer != "F"):
  
    # Prompt user for input
    answer = input("  Please enter T for True or F for False: ")

  # Give 1 point if user made the correct entry 
  if(answer == answers[num]):
    exact += 1

  # Proceed to the next question(s)
    note += 1
  print()

# Display to user # of questions they got right
print(f"You got {exact} out of {len(questions)} correct! Thanks for playing!")