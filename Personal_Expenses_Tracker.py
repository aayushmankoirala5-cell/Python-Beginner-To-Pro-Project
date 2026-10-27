import json
def Personal_Expenses_Tracker_Application():

    Total_income = 0
    Total_expenses = 0

    Income_catagories  = ["Salary","Freelance","Investment"]

    Expenses_catagories = ["Rent","Food","Utilities","Entertaiment"]

    file_path = "tracket_data.json"

    emoji = {
            "done"   :"✅",
            "caution":"⚠️",
            "wrong"  :"❌",
            "see"    :"👀",
            "cash"   :"💵",
            "online" :"🏦"
            }

    def Welcome_Msg():
        print("Welcome To Personal Expenses Tracker Application")

    def Application_info():
        print("This Application is Devloped to Track Your Daily Personal Expenses :")

    def Developer_info():
        print(
                 "This Application is Developed by : Aayushman Koirala\n"

                 "Application is deveoped in 10/27/2026 "
            )

    def line():
        print("=" *40)


    def Menu():
        line()
        Welcome_Msg()
        Application_info()
        Developer_info()
        line()
        print("")
        print("You can Use the Following Catagories  or create your own")

        # income catagory
        line()
        print("INCOME CATAGORIES IS SHOWN BELOW :")
        line()

        for i, catagory in enumerate(Income_catagories,start=1):
            print(f"{i}.{catagory}")

        #expenses catagory
        line()
        print("Expenses Catagory is Shown Below :")
        line()

        for i , catagory in enumerate(Expenses_catagories,start=1):
            print(f"{i}.{catagory}")

    def Show_Income_catagories():
        for i, catagory in enumerate(Income_catagories,start=1):
            print(f"{i}.{catagory}")

    def Show_Expenses_Catagories():
        for i ,catagory in enumerate(Expenses_catagories,start=1):
            print(f"{i}.{catagory}")

    def Devloper_mode():
        print("What would like to do (Add Income Catagory/ Add Expenses Catagory Add Income/Add Expenses/Save/Load/Exit) : ")

    def get_input():
        while True:
            try:
                choice = input("").lower()

                if choice == "add income catagory":
                    Add_income_catagory()
                    Devloper_mode()
                    

                elif choice =="add expenses catagory":
                    Add_expenses_catagory()
                    Devloper_mode()
                    

                elif choice == "add income":
                    Add_income()
                    Devloper_mode()

                elif choice == "add expenses":
                    Add_Expenses()
                    Devloper_mode()

                elif choice =="save":
                    save()
                    Devloper_mode()

                elif choice =="load":
                    Load()
                    Devloper_mode()

                elif choice =="exit":
                    print("Good Bye See You Soon : ")
                    break
                

                else:
                    print("Invaild choice,please Enter again !")
                    continue

            except ValueError:
                print("Invaild Choice :")
    
    def linebreaker():
        print("")



    def  Add_income_catagory():
        while True:
            linebreaker()
            print(f"This Following catagories are already pre existed {emoji['see']}")
            linebreaker()
            line()
            Show_Income_catagories()
            line()
            linebreaker()
            catagory = input(f"Enter the Catagorty you want to Add in INCOME :(type  Exit  to stop ) ")

            if catagory.lower() =="exit":
                break

            elif catagory.strip() == "":
                print(f"Catagory cannot be empty : {emoji['wrong']}")
            else:
                Income_catagories.append(catagory)
                

    def Add_expenses_catagory():
        while True:
            linebreaker()
            print(f"This Following catagories are already pre existed {emoji['see']}")
            linebreaker()
            line()
            Show_Expenses_Catagories()
            line()
            linebreaker()
            
            catagory = input("Enter the catagory you want to Add in Expenses :(type exit to stop)  : ")

            if catagory.lower() == "exit":
                print(f"You Reject to Add the New Expenses_catagory{emoji['wrong']} :")
                break
            
            
            

            elif catagory.strip() =="":
                print(f"Catagory cannot be empty{emoji['caution']}")

            else:
                Expenses_catagories.append(catagory)

    def Add_income():
            nonlocal Total_income
            while True:
        
                    print(f"Please select the Catagories(type exit to stop)")
                    Show_Income_catagories()
    
                    choice = input("Enter the catagories : 1 2 3 ...(type exit to stop :")
    
                    if choice.lower() == "exit":
                        print("Program Terminated :")
                        break
    
                    try:
    
                        choice = int(choice)
    
                        index = choice - 1
    
                        if index < 0 or index >=len(Income_catagories):
                            print("Invaild choice")
                            continue
    
                        print(f"You choice{Income_catagories[index]} ")
    
                        added_money = float(input("Enter the Money you want to add : "))
    
                        if added_money <=0:
                            print("Added Money Must be Greater than 0")
                            continue
    
                        Total_income += added_money
    
                        print(f"Money added successfully {emoji['done']}")
                        print(f"Total Money :{Total_income} {emoji['cash']}")
    
                    except ValueError:
                        print("Invaild Input ! Enter a Vaild Choice ")
    
                       
    
                       

    def Add_Expenses():
        nonlocal Total_expenses
            
    
        while True:
    
            choice = input(f"Please select  the catagories eg 1,2,3 ... (type exit to stop) : ")
    
            if choice.lower() == "exit":
                print(f"Program Terminated {emoji['caution']}:")
                break
    
            try:
                    choice = int(choice)
    
                    index = choice -1
    
    
    
                    if index <0 or index >=len(Expenses_catagories):
                        print(f"Invaild choice {emoji['wrong']}")
                        continue
    
                
    
                    print(f"You choice {Expenses_catagories[index]}")
    
                    expeses  = float(input("Enter the Expeses :"))
    
                    Total_expenses += expeses
     
            except ValueError:
                    print("something Went wrong :")

    def save():
        data = {
                "Total_income"  :Total_income,
                "Total_Expenses":Total_expenses,
                "Income_Catagory":Income_catagories,
                "Expenses_Catagory":Expenses_catagories,
            }
        

        with open(file_path,"w",encoding="utf-8")as file:
             json.dump(data,file,indent=4)
        print(f"Save successful{emoji['done']}")

    
    def Load():
        nonlocal Total_income, Total_expenses

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            Total_income = data["Total_income"]
            Total_expenses = data["Total_Expenses"]

            Income_catagories[:] = data["Income_Catagory"]
            Expenses_catagories[:] = data["Expenses_Catagory"]

            print(f"\nData Loaded Successfully {emoji['done']}")
            line()
            print(f"Total Income   : Rs. {Total_income:.2f}")
            print(f"Total Expenses : Rs. {Total_expenses:.2f}")
            print(f"Available Balance: Rs. {Total_income - Total_expenses:.2f}")

            print("\nIncome Categories:")
            Show_Income_catagories()

            print("\nExpense Categories:")
            Show_Expenses_Catagories()
            line()

        except FileNotFoundError:
            print("No saved file found! Save your data first.")

        except json.JSONDecodeError:
            print("The JSON file is damaged or contains invalid data.")

        except KeyError:
            print("Some required data is missing from the file.")
   


    #mainfunction

    def MainProgram():
        Devloper_mode()
        get_input()
        


    MainProgram()

Personal_Expenses_Tracker_Application()