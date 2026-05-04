#Expense Tracker Project

expenses = [] #list of expenses

print("Welcome to the Expense Tracker!")

while True:
    print("====Main Menu===")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. View total khorosh")
    print("4. Exit")


    choice = int(input("Enter your choice :"))

#Add Expense
    if (choice == 1):
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        category = input("Enter the category of the expense (e.g., Food, Transport, Entertainment): ")
        description = input("Enter a description for the expenses:")
        amount = float(input("Enter the amount of the expense: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expenses.append(expense) 

        print("\nExpense is added successfully!")


#view all expenses

    elif(choice == 2):
        if(len(expenses)==0):
            print("no expenses to show")
        else:
            print("====Expenses List====")
            
            count = 1

            for acc in expenses:
                print(f"{count}. Date: {acc['date']}, Category: {acc['category']}, Description: {acc['description']}, Amount: {acc['amount']}")
    

    #view total khorosh
    elif(choice == 3):

        total = 0
        for acc in expenses:
            total += acc["amount"]
        print(f"\nTotal khorosh: {total}")

    #exit
    elif(choice == 4):
        print("Exiting the Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
