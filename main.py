import operation as op
def menu():
    print("\tWelcome to Our Bank\t".center(50, "*"))
    print("1. Create Account")
    print("2. Show Statement")
    print("3. Transfer Money")
    print("4. Withdraw Money")
    print("5. Deposite Money")
    print("6. Show Balance")
    print("7. Delete Account")
    print("8. Exit")
    opt = int(input(("Select any option : ")))
    return opt
def main():
    while True:
        option = menu()
        if(option == 1): op.createAccount()
        elif (option == 2): op.showStatement()
        elif(option == 3): op.transferMoney()
        elif(option == 4): op.withdrawMoney()
        elif(option == 5): op.depositeMoney()
        elif(option == 6): op.showBalance()
        elif(option == 7): op.deleteAccount()
        elif(option == 8): exit()
        else: print("Please Enter valid number")
if __name__ == "__main__":
    main()