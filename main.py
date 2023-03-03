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

# Display question
print(questions[0])

# Check user entered only "T" or "F"
answer = ""

while(answer != "T" and answer != "F"):
  
  # Prompt user for input
  answer = input("  Please enter T for True or F for False: ")

# Check user entered correctly and give 1 point 
if(answer == answers[0]):
  exact += 1
else:
  exact

# Proceed to the next question
  note += 1
print()

print(questions[1])

# Check user entered only "T" or "F"
answer = ""

while(answer != "T" and answer != "F"):
  # Prompt user for input
  answer = input("  Please enter T for True or F for False: ")

# Give 1 point if user made the correct entry
if(answer == answers[1]):
  exact += 1
else:
  exact

  # Proceed to the next question
  note += 1
print()
  
# Display next question
print(questions[2])

# Check user entered only "T" or "F"
answer = ""

while(answer != "T" and answer != "F"):
  # Prompt user for input
  answer = input("  Please enter T for True or F for False: ")
  
# Give 1 point if user made the correct entry 
if(answer == answers[2]):
  exact += 1
else:
  exact

  # Proceed to the next question
  note += 1
print()

# Display next question
print(questions[3])
  
# Check user entered only "T" or "F"
answer = ""

while(answer != "T" and answer != "F"):
  # Prompt user for input
  answer = input("  Please enter T for True or F for False: ")
  
# Give 1 point if user made the correct entry 
if(answer == answers[3]):
  exact += 1
else:
  exact

  # Proceed to the next questions
  note += 1
print()

# Display next question
print(questions[4])
  
answer = ""

while(answer != "T" and answer != "F"):
  # Re-prompt user to enter T or F
  answer = input("  Please enter T for True or F for False: ")
  
if(answer == answers[4]):
  exact += 1
else:
  exact

  note += 1
  

print()

# Display to user # of questions they got right
print(f"You got {exact} out of {len(questions)} correct! Thanks for playing!")