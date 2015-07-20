import json
import DB

database = DB.connTestDB()
cursor = database.cursor()

print "Connected to database and cursor initialized."

DB.clearDB(database)

print "Opening DatabaseJSON.json..."
# Parse JSON file.
with open('DatabaseJSON.json') as data_file:
	data = json.load(data_file)
print "DatabaseJSON.json has been successfully parsed."

# The query to add a record.
add_record = ("INSERT INTO Records "
	"(activity_id, activity_name, activity_instructions, activity_primary_muscles, activity_secondary_muscles, activity_lift_type, activity_rating, activity_equipment, image_0, image_1, url)  "
	"VALUES ")

# Add the appropriate number of records.
add_record += "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"	
for row in data['data']:

	# Result Row, URL, activity_name, activity_instructions
	# activity_primary_muscle_group, muscle_0, Activity equipment
	# activity_image_0, activity_image_1, activity_lift_type
	# activity_video, activity_rating
	
	# Save to temporary variables.
	activity_id = int(float(row['Result Row']))

	# Print row being parsed.
	if activity_id % 10 == 0:
		print "\tCurrently adding activity_id: " + row['Result Row']	

	name = row['activity_name']
	instructions = row['activity_instructions']
	primary = row['activity_primary_muscle_group']
	secondary = row['muscle_0']
	equipment = row['Activity equipment']
	imageZero = row['activity_image_0']
	imageOne = row['activity_image_1']
	liftType = row['activity_lift_type']
	video = row['activity_video']
	rating = row['activity_rating']
	url = row['URL']

	# Create tuple to be added to the database.	
	newRecord = (
		activity_id,
		name,
		instructions,
		primary,
		secondary,
		liftType,
		rating,
		equipment,
		imageZero,
		imageOne,
		url
	)

	cursor.execute(add_record, newRecord)

# Commit the changes to the database.
database.commit()
print "Changes have been commited."

# Close the cursor and the database.
cursor.close()
database.close()

print "Database and cursor have been closed."
