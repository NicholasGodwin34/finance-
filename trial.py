import mysql.connector as mc 

def run():
        db=mc.connect(
              host="localhost",
              user="x",
              passwd="x",
              database="Users_info"
        )
        mine = db.cursor()
        print("Enter Your USER ID")
        userID = input("->")
        query = f"SELECT userID FROM accounts "
        mine.execute(query)
        results = [result[0] for result in mine.fetchall()]
        array = []
        print(results)
        
        

run()
