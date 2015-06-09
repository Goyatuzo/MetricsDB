import json

from pprint import pprint

# Open the activityList json file.
filename = open("activityList.json")

# Parse it as a json file.
jsonData = json.load(filename)

# Close the file.
filename.close()

for data in jsonData["data"]:
	# Just alias the video URL and edit directly.
	videoURL = data["activity_video"][0].encode("ascii")
	
	# Find the index where "videocdn" first appears.
	cdnIDX = videoURL.find("videocdn")
	# Find the index where .mp4 last appears and the video URL is found.
	mp4IDX = videoURL.find(".mp4")
	
	# Substring of the cdn index to the end and append http.
	videoURL = "http://" + videoURL[cdnIDX:mp4IDX+4]
	
	data["activity_video"][0] = videoURL.decode("ascii")

# Open the new file to be written to.	
filename = open("activityEdit.json", "w")

# Dump the information.
json.dump(jsonData, filename)