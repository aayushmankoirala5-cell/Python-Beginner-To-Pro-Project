import random

def line():
    print("===========================")

emoji = {
        "r" :"🪨",
        "p" : "📃",
        "s" :"✂️"
        }

choice  = tuple(emoji.keys())


line()
print("Welcome to the Rock Paper Scissors Game ")
print("Choice The Game Set [MUST BE IN ODD]    ")
line()


Game_set = int(input("Enter the game set Eg : 1 , 3 , 5 ... : "))

Winning_Target = (Game_set // 2) +  1

user_win_counter = 0

computer_win_counter = 0


while (True):

    try:

        if Game_set > 0 and Game_set %2 !=0:
            print(f"Game Set Has Been Registred : {Game_set}")
            break

        else:
            print("Invaild Choice :")

    except ValueError:
        print("Invaild Choice :")

while (
    Game_set > 0
      and user_win_counter < Winning_Target
      and computer_win_counter < Winning_Target
    ):

    user_choice = input("Enter the Choice ie : r , p ,  s : ").lower()

    if user_choice not in choice:
        print("Invaild choice , Choice Again :")
        continue


    Computer_choice = random.choice(choice)

    print(f"You choice :{emoji[user_choice]}")
    print(f"Computer Choice :{emoji[Computer_choice]}")

    if user_choice == Computer_choice:
        print(" Tie!")
        Game_set -=1

    elif (
            (user_choice == "r" and Computer_choice =="s")
            or(user_choice == "p" and Computer_choice =="r")
            or(user_choice == "s" and Computer_choice =="p")

        ):
        
        print(" You Win This Round !")

        user_win_counter += 1
        Game_set -=1

    else:
        print("/n Computer Win Thi Round !")
        Game_set -=1


print("============================================================")

print("====================== Final Result ========================")

print("=============================================================")

if(user_win_counter == computer_win_counter):
    print("Tie !")

elif user_win_counter > computer_win_counter:
    print("YOU WIN !")

else:
    print("Computer Win")



    



    






    