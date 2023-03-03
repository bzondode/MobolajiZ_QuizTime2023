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
print("Welcome to Quiz Time! You will answer a few True or False questions. Please ONLY enter the letter T or F when it is your turn to answer. Have fun!")

# Create variable to keep track of correct guesses
exact = 0

# Create variable to keep track of whre we are
note = 0

# Store questions and answers in variables
questions = ("Q1. There are seven continents in the world", "Q2. Insects have six legs", "Q3. The Earth is the closest planet to the Sun")
answers = ("T", "T", "F")

answer = ""

# Loop through questions
while(answer != "T" and answer != "F"):
  
  # Display question
  print(questions[0]) 
  
  # Prompt user for input
  answer = input("Please enter T for True or F for False: ")

# Check user entered correctly and give point (1) accordingly 
if(answer == answers[note]):
  exact += 1

# Proceed to the next question
  note += 1

  # Display next question
  print(questions[1]) 
  
  # Prompt user for input
  answer = input("Please enter T for True or F for False: ")
# Check user entered correctly and give point (1) accordingly 
if(answer == answers[note]):
  exact += 1

# Proceed to the next question
  note += 1
 
  # Display next question
  print(questions[2])
  
  # Prompt user for input
  answer = input("Please enter T for True or F for False: ")
  
# Check user entered correctly and give point (1) accordingly 
if(answer == answers[note]):
  exact += 1

  note += 1
  
# Display to user # of questions they got right
print(f"You got {exact} out of {len(questions)} correct! Thanks for playing!")