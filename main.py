import mysql.connector as mc


class ATM():
    def __init__(self, initial_balance=0) :
        self.balance = initial_balance

        pass
    def create_account(self):

        try:
            db=mc.connect(
                host="localhost",
                user="Nicholas",
                passwd="nicholas",
                database="Users_info")
                                    
            mine = db.cursor()

            email = input("Enter your email: ")
            f_name = input("Enter your first name: ")
            S_name = input("Enter your second name: ")
            age = int(input("Enter your age: "))
            balance =  0
            phone_number = input("Enter your mobile number: ")
            if age < 18: 
                print("You must be 18+!")
            else:
                query = ("INSERT INTO accounts(email,first_name, second_name, age, phone_number) VALUES (%s,%s,%s,%s,%s)" )
                data = (str(email), str(f_name), str(S_name), str(age), str(phone_number))
                mine.execute(query,data)
                db.commit()
                
                def create_pin(userID):
                    print("Enter a 4 digit pin")
                    pin = input(">")
                    if not pin.isdigit():
                        create_pin()
                    else: 
                        query1 = ('INSERT INTO pins( userID , pin ) VALUES (%s,%s)')
                        data1 = (userID, pin)
                        mine.execute(query1,data1)
                        db.commit()

                create_pin()


        except mc.Error as err:
            print(f"Error: {err}")

        finally:
            if  db.is_connected():
                mine.close()
                db.close()
                print("MySql has been closed ")

        
    def check_balance(self):
        db=mc.connect(
                host="localhost",
                user="Nicholas",
                passwd="nicholas",
                database="Users_info")
                                    
        mine = db.cursor()
        userID = input("Enter your user ID: ")
        trial = 0
        if trial == 0:
            try:
                userID = int(userID)
                trial += 1
            except ValueError:
                print("Invalid input. User ID has to be an integer.")   
                return   
        query = ("SELECT balance FROM accounts WHERE userID = %s")
        data = (userID,)
        mine.execute(query,data)
        result = mine.fetchone()

    

        db.close()

        print(f"Your balance is: {result[0]} ")

    def deposit(self,amount):
        db=mc.connect(
                host="localhost",
                user="Nicholas",
                passwd="nicholas",
                database="Users_info")
                                    
        mine = db.cursor()
        userID = input("Enter your user ID: ")
        print("Enter the amount to deposit")
        amount(input ("->"))

        query = ("UPDATE accounts SET balance = balance + %s where userID = %s" )
        data = (amount, userID)

        mine.execute(query,data)
        db.commit()
        db.close()
        

        pass 
    def withdraw(self):
        db=mc.connect(
                host="localhost",
                user="Nicholas",
                passwd="nicholas",
                database="Users_info") 
                                    
        mine = db.cursor()
        userID = input("Enter your user ID: ")
        print("Enter amount to withdraw ")
        withdraw = input("->")
        
        
        query = ("UPDATE accounts SET balance = balance - %s where userID = %s" )
        data = (withdraw, userID)

        mine.execute(query, data)
        db.commit()
        mine.close()
        db.close()


        pass 
    def run(self):
        print("Enter Your USER ID")
        userID = input("->")
        #if userID in 
        while True:
            print("\n ATM menu")
            print("\n 1. Check balance")
            print("\n 2. Withdraw Money")
            print("\n 3. Deposit Money")
            print("\n 4. Exit")
            
        pass 



# ATM.check_balance()

object = ATM

def main():
    object