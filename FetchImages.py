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
	# Make sure that imgOne or imgTwo are not null..
	if imgOne:
		# There may be threading errors. Hopefully not anymore.
		try:
			results.append(urllib.urlretrieve(imgOne, dirname + name + "-1.png"))
			# Check to see an image was downloaded. If not, download medium instead.
			if os.stat(dirname + name + "-1.png").st_size == 0:
				print "\t" + "IMG 1: Large for " + name + " does not exist. Downloading medium."
				# Replace 960,960 with 480,480
				medOne = imgOne.replace("960,960", "480,480")
				results.append(urllib.urlretrieve(medOne, dirname + name + "-1.png"))
		except:
			print "\t\tIMG 1: " + name + " has an error."
	# Make sure the image exists.
	if imgTwo:
		# There may be threading errors. Hopefully not anymore.
		try:
			results.append(urllib.urlretrieve(imgTwo, dirname + name + "-2.png"))
			if os.stat(dirname + name + "-2.png").st_size == 0:
				print "\t" +"IMG 2: Large for " + name + " does not exist. Downloading medium."
				# Replace 960,960 with 480,480
				medTwo = imgTwo.replace("960,960", "480,480")
				results.append(urllib.urlretrieve(medTwo, dirname + name + "-2.png"))
		except:
			print "\t\tIMG 2: " + name + " has an error."
		

# Keep counter to print out name every 10 images.
for image in cursor:
	while threading.active_count() > 10:
		time.sleep(1)

	# Set each query item a variable name to be called into the thread.
	name = image[0].lower().replace(' ', '-')
	imgOne = image[1]
	imgTwo = image[2]

	print name

	# Retrieve each image through a thread.
	t = threading.Thread(target = getImage, args = (name, imgOne, imgTwo))
	t.start()
	threads.append(t)
	# Wait one second or else too many files will be open.
	time.sleep(0.5)

#while threading.active_count > 0:
#	time.sleep(0.2)

map(lambda t: t.join(), threads)

cursor.close()
db.close()
