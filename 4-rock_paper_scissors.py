import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choice = False
cpu_choice = random.randint(0,2)
cpu_choice = str(cpu_choice)
while (choice == False):
    user_choice = input("What would you like to choose? Rock:0, Paper:1, or Scissors:2? Type a number:")

    if user_choice == "0":
        user_choice = rock
        choice = True
    elif user_choice == "1":
        user_choice = paper
        choice = True
    elif user_choice == "2":
        user_choice = scissors
        choice = True
    else:
        print("Invalid selection, please try again")

if cpu_choice == "0":
    cpu_choice = rock
elif cpu_choice == "1":
    cpu_choice = paper
else:
    cpu_choice = scissors

print(f"""
    Users choice: 
    {user_choice}
    CPU choice:
    {cpu_choice}
    """)

if user_choice == cpu_choice:
    print("It's a draw")
elif (user_choice == rock and cpu_choice == paper) or (user_choice == paper and cpu_choice == scissors) or (user_choice == scissors and cpu_choice == rock):
    print("CPU Wins")
elif (user_choice == rock and cpu_choice == scissors) or (user_choice == paper and cpu_choice == rock) or (user_choice == scissors and cpu_choice == paper):
    print("You Win")
else:
    print("Its a draw")


