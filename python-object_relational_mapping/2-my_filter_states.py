import MySQLdb
from sys import argv
#Connect to the MySQL server
db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
#Create a cursor to execute queries
cursor= db.cursor()

#Execute the query to list states in ascending order by id
query = "SELECT * FROM states WHERE BINARY states.name='{}' ORDER BY states.id ASC".format(argv[4])
cursor.execute(query)
    
#display
results= cursor.fetchall()

#print
for row in results:
    print(row)

#close connection   
cursor.close()
db.close()
