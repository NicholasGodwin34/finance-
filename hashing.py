import bcrypt as bc 
import mysql.connector as mc 

def hash_pin(pin):
    salt = bc.gensalt()
    hashed_pin = bc.hashpw(pin.encode('utf-8'), salt)
    return hashed_pin

def store_hash(userID, pin):
    db = mc.connect(
        host='localhost',
        database='users_info',
        user='Nicholas',
        passwd='nicholas'
    )
    c=db.cursor()
    hashed_pin = hash_pin(pin)

    query = ("INSERT INTO pins(userId, pin) VALUES (%s, %s )")
    c.execute(query,(userID, hashed_pin.decode('utf-8')))
    db.commit()
    c.close()
    db.close()



#store_hash(userID,pin)

def verify_pin(stored_hash, input_pin):
    return bc.checkpw(input_pin.encode('utf-8'), stored_hash)

def check_user_pin(userID, input_pin):
    db = mc.connect(
        host='localhost',
        database= 'users_info',
        user='Nicholas',
        passwd='nicholas'
    )

    c = db.cursor()
    query = "SELECT pin FROM pins WHERE userId = %s"
    c.execute(query,(userID,))
    result = c.fetchone()
    stored_hash = str(result[0])

    db.close()

    return verify_pin(stored_hash.encode('utf-8'),input_pin)

