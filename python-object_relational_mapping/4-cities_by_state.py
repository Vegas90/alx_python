import MySQLdb
from sys import argv
#Connect to the MySQL server
db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
#Create a cursor to execute queries
cursor= db.cursor()

#Execute the query 
query = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id  ORDER BY cities.id ASC"
# Put the parameter in a tuple 
cursor.execute(query)
    
#display
results= cursor.fetchall()

#print
for row in results:
    print(row)

#close connection   
cursor.close()
db.close()
