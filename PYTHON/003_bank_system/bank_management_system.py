accounts = {}

def create_account():
    acc_no = input("Enter account number: ")
    name = input("Enter name: ")
    balance = float(input("Enter initial balance: "))

    accounts[acc_no] = {
        "name": name,
        "balance": balance
    }

    print("Account created successfully!")

def deposit():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_no]["balance"] += amount
        print(f"Rs. {amount} deposited successfully!")
    else:
        print("Account not found.")

def withdraw():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount 
            print(f"Rs. {amount} withdrawn successfully!")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")

def check_balance():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        print(f"Balance: Rs. {accounts[acc_no]['balance']}")
    else:
        print("Account not found.")

def delete_account():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        del accounts[acc_no]
        print("Account deleted successfully!")
    else:
        print("Account not found.")


while(True):
    print("\n====== BANK MANAGEMENT SYSTEM ======")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Delete Account")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if not choice.isdigit():
        print("Please enter valid choice: ")
        continue

    choice = int(choice)

    if choice == 1:
        create_account()

    elif choice == 2:
        deposit()

    elif choice == 3:
        withdraw()

    elif choice == 4:
        check_balance()

    elif  choice == 5:
        delete_account()

    elif choice == 6:
        print("Thank you for using bank system.")
        break
    else:
        print("Invalid choice")