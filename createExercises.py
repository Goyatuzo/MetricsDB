import csv
import random


def gen_rand_reps():
    reps = ""

    for i in range(0, random.randint(1, 10)):
        reps += str(random.randint(1, 10)) + ","

    return reps[:-1]


# Generate the file and configure the writer.
f = open("exercises.csv", "w")
writer = csv.writer(f, quoting=csv.QUOTE_ALL)
writer.writerow(['reps', 'rest_time', 'type', 'window_range', 'record'])

# Construct the exercist list.
exercises = []

# The currently available list of types.
types = [
    'Burnout',
    'Dropset',
    'Standard',
    'Pyramid',
    'Five'
]

# Generate 50 random entries.
for i in range(50):
    rand_reps = gen_rand_reps()
    rand_rest = int(random.randint(1, 20))
    rand_type = types[random.randint(0, 4)]
    rand_window = random.randint(1, 15)
    rand_record = random.randint(1, 200)

    writer.writerow([rand_reps, rand_rest, rand_type, rand_window, rand_record])