import MySQLdb
from sys import argv
#Connect to the MySQL server
db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
#Create a cursor to execute queries
cursor= db.cursor()

#Execute the query 
query = "SELECT states.name, cities.name FROM cities INNER JOIN states ON cities.state_id = states.id  WHERE states.name= %s ORDER BY cities.id ASC"
param= (argv[4])
# Put the parameter in a tuple 
cursor.execute(query, param)
    
#display
results= cursor.fetchall()

#print
for row in results:
    print(row)

#close connection   
cursor.close()
db.close()
