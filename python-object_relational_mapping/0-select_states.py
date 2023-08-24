#content
import MySQLdb

#connection
db=MySQLdb.connect(host="localhost", port=3306, user="username", passwd="password", db="hbtn_0e_0_usa")

# Create a cursor to execute queries
cursor= db.cursor()

cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

#RESULTS
results= cursor.fetchall()
#print
for row in results:
    print(row)

#close connection   
cursor.close()
db.close()
