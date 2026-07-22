import random

print("Welcome to Rock-Paper-Scissors!")

user_score = 0
comp_score = 0
round_num = 1

choice_names = {"R": "Rock", "P": "Paper", "S": "Scissors"}

while True:
    print(f"\n -----Round {round_num}-----")
    
    # Input validation for user choice
    while True:
        user_choice = input("Press R for rock, P for paper, or S for scissors: ").strip().upper()
        
        if user_choice in ["R", "P", "S"]:
            break
        print("Invalid choice. Allowed Input: R for rock, P for paper, or S for scissors")
        
    comp_choice = random.choice(["R", "P", "S"])
    
    print(f"You chose: {choice_names[user_choice]}")
    print(f"Computer chose: {choice_names[comp_choice]}")
    
    # Determine winner
    if user_choice == comp_choice:
        print("It's a tie!")
        
    elif (user_choice == "R" and comp_choice == "S") or \
         (user_choice == "S" and comp_choice == "P") or \
         (user_choice == "P" and comp_choice == "R"):
        print("You win!")
        user_score += 1
        
    else:
        print("Computer wins!")
        comp_score += 1
        
    print(f"Score: You {user_score} Computer {comp_score}")
    
    # Continue prompt validation
    while True:
        again = input("Do you want to play another round? (Y/N): ").strip().upper()
        if again in ["Y", "N"]:
            break
        print("Invalid choice. Please enter Y or N.")
        
    if again == "N":
        break
        
    round_num += 1

print("\nGame Over!")
print(f"Final Score: You {user_score} Computer {comp_score}")

if user_score > comp_score:
    print("You won the game!")
elif comp_score > user_score:
    print("Computer won the game!")
else:
    print("The game ended in a tie!")