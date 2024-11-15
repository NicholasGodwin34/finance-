import mysql.connector as mc
from hashing import store_hash, check_user_pin
from binarySearch import sort, bsa

def create_account():
    db = mc.connect(
        host="localhost",
        user="Nicholas",
        passwd="nicholas",
        database="users_info")

    mine = db.cursor()

    email = input("Enter your email: ")
    f_name = input("Enter your first name: ")
    S_name = input("Enter your second name: ")
    age = int(input("Enter your age: "))
    phone_number = input("Enter your mobile number: ")
    if age < 18:
        print("You must be 18+!")
    else:
        query = "INSERT INTO accounts(email,first_name, second_name, age, phone_number) VALUES (%s,%s,%s,%s,%s)"
        # data = (str(email), str(f_name), str(S_name), str(age), str(phone_number))
        data = (email,f_name, S_name, age, phone_number)
        mine.execute(query, data)


    query1 = 'select userID from accounts where email = %s'
    data1 = (email,)
    mine.execute(query1,data1)
    
    result = mine.fetchone()
    print(f"Your User ID is: {result[0]}")


    db.commit()
    def create_pin(userID):
            print("Enter a 4 digit pin")
            pin = input(">")
            if not pin.isdigit():
                create_pin()
            else: 
                store_hash(userID,pin)
                           

    create_pin(result[0])

    db.close()


def deposit():
        db = mc.connect(
             host="localhost",
             user="Nicholas",
             passwd="nicholas",
             database="users_info"
        )
        mine =db.cursor()
        #get users input and check the userID with the ones in the database for transaction 
        userID = input("Enter your user ID:: ")
        while True: 
            pin = input("Enter you pin:: ")
        
            if check_user_pin(userID, pin):
                print("Enter the amount to deposit")
                amount = (input ("->"))
                
                query = (f"UPDATE accounts SET balance = balance + %s where userID = %s" )
                data = (amount, userID)
                mine.execute(query,data)
            
                db.commit()
                mine.execute("SELECT balance FROM accounts where userID = %s ",(userID,))
                result = mine.fetchone()
                print(f"New balance : {result[0]}")
                db.close()
                break 
            else: 
                 print("Wrong pin.")
                 continue


def check_balance():
        db=mc.connect(
                host="localhost",
                user="Nicholas",
                passwd="nicholas",
                database="Users_info")
                                    
        mine = db.cursor()
        userID = input("Enter your user ID: ")
        pin = input("Enter Your pin: ")
        while True:
            if check_user_pin(userID, pin):
                query = (f"SELECT balance FROM accounts WHERE userID = %s")
                data = (userID,)
                mine.execute(query,data)
                result = mine.fetchone()
                db.close()
                print(f"Your balance is: {result[0]} ")
                break 
            else:
                print("Wrong pin.")
                break 

def withdraw():
        db=mc.connect(
                host="localhost",
                user="Nicholas",
                passwd="nicholas",
                database="Users_info") 
                                    
        mine = db.cursor()
        userID = input("Enter your user ID: ")
        while True:
            pin = input("Enter your pin: ")
            if check_user_pin(userID ,pin):
                print("Enter amount to withdraw ")
                withdraw = int(input("->"))
            
                check= (f'SELECT balance FROM accounts WHERE userID = %s')
                data1 = (userID,)
                mine.execute(check,data1)
                result = mine.fetchone()

                if result[0] < withdraw or result[0] == 0: 
                    print("Insufficient balance.")
                    print(f"Your balance: {result[0]}")
                else:
                    query = ("UPDATE accounts SET balance = balance - %s where userID = %s" )
                    data = (withdraw, userID)
                    mine.execute(query, data)
                    db.commit()
                    mine.execute("SELECT balance FROM accounts WHERE userID = %s", (userID,))
                    balance = mine.fetchone()

                    
                    print(f"You have withdrawn: {withdraw}")
                    print(f"Your balance: {balance[0]}")
                    break
            else:
                print("Wrong Pin.")
                continue

def run():
        db=mc.connect(
              host="localhost",
              user="Nicholas",
              passwd="nicholas",
              database="Users_info"
        )
        mine = db.cursor()
        print("Enter Your USER ID")
        userID = input("->")
        query = f"SELECT userID FROM accounts "
        mine.execute(query)
        results = [result[0] for result in mine.fetchall()]
        result = sort(results)     
        
        for i in results: 
            while True: 
                if bsa(int(userID),result):
                    print("\n ATM menu")
                    print("\n 1. Check balance")
                    print("\n 2. Withdraw Money")
                    print("\n 3. Deposit Money")
                    print("\n 4. Exit")
                    choice =input("> ")

                    if choice == '1':
                        check_balance()
                        break 
                    elif choice == '2':
                        withdraw()
                        break 
                    elif choice == '3':
                        deposit()
                        break 
                    elif choice == '4':
                        exit()
                    else:
                        print("Invalid Choice. Please try again.")
                        continue

                
                else:
                    print("Invalid Input. User ID not found!")
                    print("5. Re-enter User ID")                               
                    print("6. Create account and get User ID")
                    choice = input(">")

                    if choice == '5':
                        run()
                    elif choice == '6':
                        create_account()
                    else: 
                        print("Invalid input.")
                        exit()


        db.commit()
        mine.close()
        db.close()

#create_account()
run()

#withdraw()
#deposit()
#check_balance()