import os
from datetime import datetime
p_ath = "./bank_account/" 
statement_path = "./account_statement/"
# Create Account
def createAccount():
    customerName = input("Enter your name : ")
    customerMobile = input("Enter the mobile number : ")
    customerFather = input("Enter your father name : ")
    openingAmount = input("Enter amount for open account : ")
    loginPassword = input("Create login password : ")
    transactionPassword = input("Create transaction password")
    try:
        accountNumber = "ACB"+ customerMobile
        account = p_ath + accountNumber + ".txt"
        if not os.path.exists(account):
            createAccount = open(account, "w")
            # Format -> accountNumber,customerName,MobileNumber,FatherName,Amount,loginPassword,transactionPassword
            createAccount.write(accountNumber + "," + customerName + "," + customerMobile + "," + customerFather + "," + openingAmount + "," + loginPassword + "," + transactionPassword)
            statement = open(statement_path + accountNumber + ".txt", "w")
            #StatementFormat -> Date/Time,ThroughBy,Type,Cr,Db,TotalAmount
            date = datetime.now()
            statement.write(date.strftime("%d/%m/%Y %H:%M:%S" + "," + "open" + "," + "deposite" + "," + openingAmount + "," + "0" + "," + openingAmount + "\n"))
            createAccount.close()
            statement.close()
            print("\tAccount Successfully Created\t".center(50, "="))
        else:
            print("\tAccount is already Exists\t".center(50, "!"))
    except:
        print("\tAccount not create from internal error\t".center(50, "!"))

# Delete Account
def deleteAccount():
    try:
        accountNumber = input("Enter the account number : ")
        if os.path.exists(p_ath + accountNumber + ".txt"):
            os.remove(p_ath + accountNumber + ".txt")
            print("\tAccount Successfully deleted\t".center(50, "="))
        else:
            print("\tAccount is not exist to database\t".center(50,"!"))
    except:
        print("\tAccount not deleted from internal error\t".center(50, "!"))

# Show total amount of account
def showBalance():
    try:
        accountNumber = input("Enter the account number : ")
        if os.path.exists(p_ath + accountNumber + ".txt"):
            loginPassword = input("Enter the login password : ")
            accountInfo = open(p_ath + accountNumber + ".txt", "r")
            accountInfo = accountInfo.read().split(",")
            if(loginPassword == accountInfo[5]):
                print("\tTotal Amount : {}\t".format(accountInfo[4]).center(50, "="))
            else:
                print("\tInvalid Credentials\t".center(50, "!"))                
        else:
            print("\tAccount is not exist to database\t".center(50,"!"))
    except:
        print("\tBalance not show from internal error\t".center(50, "!"))

# Deposite Amount
def depositeMoney():
    try:
        print("\tLogin now\t".center(50, "="))
        accountNumber = input("Enter your account number : ")
        loginPassword = input("Enter your password : ")
        accountBook = p_ath + accountNumber + ".txt"
        if os.path.exists(accountBook):
            accountFile = open(accountBook, "r+")
            accountInfo = accountFile.read().split(",")
            if(accountInfo[5] == loginPassword):
                depositeMoney = input("Enter the deposite money : ")
                statement = open(statement_path + accountNumber + ".txt", "a")
                #StatementFormat -> Date/Time,ThroughBy,Type,Cr,Db,TotalAmount
                date = datetime.now()
                statement.write(date.strftime("%d/%m/%Y %H:%M:%S" + "," + "self" + "," + "deposite" + "," + depositeMoney + "," + "0" + "," + str(int(accountInfo[4])+int(depositeMoney))+ "\n"))
                accountInfo[4] = str(int(accountInfo[4]) + int(depositeMoney))
                accountInfo = ",".join(accountInfo)
                accountFile.seek(0)
                accountFile.write(accountInfo)
                statement.close()
                accountFile.close()
                print("\tAmount Deposite Successfully\t".center(50, "="))
            else:
                print("\tInvalid Crediential\t".center(50,"!"))
        else:
            print("\tAccount is not found\t".center(50, "!"))
    except:
        print("\tMoney not deposite from internal error\t".center(50, "!"))

# withdraw Amount
def withdrawMoney():
    try:
        print("\tLogin now\t".center(50, "="))
        accountNumber = input("Enter your account number : ")
        loginPassword = input("Enter your password : ")
        accountBook = p_ath + accountNumber + ".txt"
        if os.path.exists(accountBook):
            accountFile = open(accountBook, "r+")
            accountInfo = accountFile.read().split(",")
            if(accountInfo[5] == loginPassword):
                withdrawMoney = input("Enter the deposite money : ")
                statement = open(statement_path + accountNumber + ".txt", "a")
                #StatementFormat -> Date/Time,ThroughBy,Type,Cr,Db,TotalAmount
                date = datetime.now()
                statement.write(date.strftime("%d/%m/%Y %H:%M:%S") + "," + "self" + "," + "withdraw" + "," + "0" + "," + withdrawMoney + "," + str(int(accountInfo[4])-int(withdrawMoney))+ "\n")
                accountInfo[4] = str(int(accountInfo[4]) - int(withdrawMoney))
                accountInfo = ",".join(accountInfo)
                accountFile.seek(0)
                accountFile.write(accountInfo)
                statement.close()
                accountFile.close()
                print("\tAmount withdraw Successfully\t".center(50, "="))
            else:
                print("\tInvalid Crediential\t".center(50,"!"))
        else:
            print("\tAccount is not found\t".center(50, "!"))
    except:
        print("\tMoney not withdraw from internal error\t".center(50, "!"))

# Transfer Money
def transferMoney():
    try:
        print("\tLogin now\t".center(50, "="))
        accountNumber = input("Enter your account number : ")
        loginPassword = input("Enter your password : ")
        sAccountBook = p_ath + accountNumber + ".txt"
        if os.path.exists(sAccountBook):
            sAccountFile = open(sAccountBook, "r+")
            sAccountInfo = sAccountFile.read().split(",")
            if (loginPassword == sAccountInfo[5]):
                rAccountNumber = input("Enter the another client account number ")
                transactionPassword = input("Enter the transaction password : ")
                if(sAccountInfo[6] == transactionPassword):
                    rAccountBook = p_ath + rAccountNumber + ".txt"
                    if os.path.exists(rAccountBook):
                        rAccountFile = open(rAccountBook, "r+")
                        rAccountInfo = rAccountFile.read().split(",")
                        transferMoney = input("Enter the transfer money : ")
                        sStatement = open(statement_path + accountNumber + ".txt", "a")
                        rStatement = open(statement_path + rAccountNumber + ".txt", "a")
                        date = datetime.now()
                        sStatement.write(date.strftime("%d/%m/%Y %H:%M:%S") + "," + "self/transfer to" + rAccountNumber + "," + "transfer" + "," + "0" + "," + transferMoney + "," + str(int(sAccountInfo[4]) - int(transferMoney))+ "\n")
                        rStatement.write(date.strftime("%d/%m/%Y %H:%M:%S") + "," + "transfer by " + accountNumber + "," + "transfer" + "," + transferMoney + "," + "0" + "," +  str(int(rAccountInfo[4]) + int(transferMoney))+ "\n")
                        sAccountFile.seek(0)
                        rAccountFile.seek(0)
                        sAccountInfo[4] = str(int(sAccountInfo[4]) - int(transferMoney))
                        rAccountInfo[4] = str(int(rAccountInfo[4]) + int(transferMoney))
                        rAccountInfo = ",".join(rAccountInfo)
                        sAccountInfo = ",".join(sAccountInfo)
                        sAccountFile.write(sAccountInfo)
                        rAccountFile.write(rAccountInfo)
                        sAccountFile.close()
                        rAccountFile.close()
                        print("\tMoney Successfully transfer\t".center(50, "!"))
                    else:
                        print("\tPlease provide the valid account number of another user\t".center(50, "!"))
                else:
                    print("\tPlease provide the valid transaction password\t".center(50, "!"))
            else:
                print("\tInvalid Credentails\t".center(50, "!"))
        else:
            print("\tAccount is not found\t".center(50, "!"))
    except:
        print("\tMoney not transfer due to internal error\t".center(50, "!"))

# Show Statement
def showStatement():
    try:
        accountNumber = input("Enter the account  number : ")
        loginPassword = input("Enter you password : ")
        account = statement_path + accountNumber + ".txt"
        if os.path.exists(account):
            bAccount = open(p_ath + accountNumber + ".txt", "r")
            bAccount = bAccount.read().split(",")
            if loginPassword == bAccount[5]:
                sAccountStatement = open(account, "r")
                print("\n\nDate Time\t\t\tThrough By\t\t\tType\t\t\tCr.\t\t\tDb.\t\tTotal Amount\n\n")
                line = sAccountStatement.readline()
                print("\t", end="")
                while line != "":
                    line = line.split(",")
                    # print("\t" + line[0] + "\t\t" + line[1] + "\t\t\t" + line[2] + "\t\t" + line[3] + "\t\t" + line[4] + "\t\t" + line[5])
                    print()
                    print(line[0].center(20, " "), end="")
                    print(line[1].center(40, " "), end="")
                    print(line[2].center(15, " "), end="")
                    print(line[3].center(30, " "), end="")
                    print(line[4].center(20, " "), end="")
                    print(line[5].center(20, " "), end="")
                    line = sAccountStatement.readline()
            else:
                print("\tInvalid Credential\t".center(50, "!"))
        else:
            print("\tAccount is not found\t".center(50, "!"))
    except:
        print("\tNot Showing statement due to internal error\t".center(50, "!"))
