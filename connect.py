import mysql.connector as mc 
from hashing import store_hash

def create(ID,pin): 
        print("Enter a 4 digit pin")
        pin = input(">")
        if not pin.isdigit():
            create()
        else: 
            store_hash(ID,pin)

        
create(15,4422)
create(16,3189)
create(17,8901)
create(18,1909)
create(19,7179)