import random

while True:
    choice = input("Enter y for Yes OR n for No: ").lower()


    if choice == "y" :

        dice1 = random.randint(1,6)

        dice2 = random.randint(1,6)

        print(f"{dice1},{dice2}")

    elif choice == "n":
        print("Thank You For Playing")
        break

    else :
        print("Invaild Choice :")
    