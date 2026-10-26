import random

print("Guess the number Choosen by System")

pick = random.randint(1,100)        

while True:

    

    choice = int(input("Predict The Number :"))

    if choice == pick :
        print(f"{choice} Is correct :")
        break
    elif choice > pick:
        print("Smaller")

    elif choice < pick:
        print("Greater")

    else:
        print("Invaild Choice")

    