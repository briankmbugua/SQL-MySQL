#!/usr/bin/python3
# """List all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys
#connect to the database(MySQL)
db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],db=sys.argv[3])
#create the cursor object
c = db.cursor()
#Executing an SQL statement
c.execute("SELECT * FROM `states`")#The result will be on the cursor object
#Usig the fetchall() method of the cursor object to fetch all the results of the query
for state in c.fetchall():
    print(state)

