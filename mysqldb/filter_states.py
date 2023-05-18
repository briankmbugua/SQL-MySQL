#!/usr/bin/python3
import MySQLdb
import sys
#should not be executed when imported
if __name__ == '__main__':
    #create connection to the database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],db=sys.argv[3])
    userInput = sys.argv[4]
    #create a cursor object
    c = db.cursor()
    sql = f"SELECT id, name FROM states WHERE BINARY name LIKE '{userInput}'"
    c.execute(sql)
    for result in c.fetchall():
        print(result)
    
