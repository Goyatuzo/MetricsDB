import DB
import urllib


# Connect to the database.
db = DB.connTestDB()

cursor = db.cursor()

# Get the thumbnail picture from the database.
query = ("SELECT image_0 FROM test.Records")
cursor.execute(query)

for image in cursor:
	

cursor.close()
db.close()
