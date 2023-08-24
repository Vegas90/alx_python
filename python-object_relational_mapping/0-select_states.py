import MySQLdb
#connection
def list_states(username, password, database):
    #Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    #Create a cursor to execute queries
    cursor= db.cursor()
    
    #Execute the query to list states in ascending order by id
    query = "SELECT * FROM hbtn_0e_0_usa.states ORDER BY states.id ASC"
    cursor.execute(query)
        
    #display
    results= cursor.fetchall()

    #print
    for row in results:
        print(row)
    #close connection   
    cursor.close()
    db.close()
