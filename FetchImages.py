import DB
import urllib
import os
import threading
import time

# Connect to the database.
db = DB.connTestDB()

cursor = db.cursor()

# Get the thumbnail picture from the database.
query = ("SELECT activity_name, image_0, image_1 FROM test.Records")
cursor.execute(query)

# If it doesn't exist, create a folder to store the images.
dirname = "./Thumbnails/"
if not os.path.isdir(dirname):
	os.mkdir(dirname)

# Create threads to make it go faster.
threads = []
results = []

def getImage(name, imgOne, imgTwo):
	print '\t' + name

	# Make sure that imgOne or imgTwo are not null..
	if imgOne:
		results.append(urllib.urlretrieve(imgOne, dirname + name + "-1.png"))
	if imgTwo:	
		results.append(urllib.urlretrieve(imgTwo, dirname + name + "-2.png"))

# Keep counter to print out name every 10 images.
for image in cursor:
	# Set each query item a variable name to be called into the thread.
	name = image[0].lower().replace(' ', '-')
	imgOne = image[1]
	imgTwo = image[2]

	# Retrieve each image through a thread.
	t = threading.Thread(target = getImage, args = (name, imgOne, imgTwo))
	t.start()
	threads.append(t)
	# Wait one second or else too many files will be open.
	time.sleep(0.1)

map(lambda t: t.join(), threads)

cursor.close()
db.close()
