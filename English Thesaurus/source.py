import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

# Navigate to the DB
curser = con.cursor()

word = input("Enter a word : ")
query = curser.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " %word)
#query = curser.execute("SELECT * FROM Dictionary")

results = curser.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("No word found.")