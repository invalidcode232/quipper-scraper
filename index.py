# Auto generates a fake university profile and its faculties

# Libraries
import json
import random

# Remove all data from results/results.txt
with open('results/results.txt', 'w') as f:
    f.write('')

# Parse json from data/data.json
with open('data/data.json') as json_file:
    data = json.load(json_file)

    for university in data['universities']:
        # Generates a random number between the 0 and length of data['connector'] and use it to get a random connector
        connector = data['connectors']['definition'][random.randint(0, len(data['connectors']['definition']) - 1)]

        # Generates a random number between the 0 and length of data['fun_facts'] and use it to get a random fun fact
        fun_fact = data['fun_facts'][random.randint(0, len(data['fun_facts']) - 1)]

        # Date of found
        # Generate date of found randomly,
        # with the minimum range specified in data['founding_date']['min'] and
        # the maximum range specified in data['founding_date']['max']
        founding_date = random.randint(int(data['founding_date']['min']), int(data['founding_date']['max']))

        # Generate a random number between 0 and 1
        style = random.randint(0, 1)

        if style == 0:
            profile = f"Didirikan pada {founding_date}, {university} {connector} {fun_fact}."
        else:
            profile = f"{university} {connector} {fun_fact} yang didirikan pada {founding_date}."

        profile += "\n Fakultas: \n"

        # Generate a random number and use it as the faculty count, then get the faculties based on the count randomly,
        # the faculties must be unique
        faculty_count = random.randint(1, len(data['faculties']))
        faculties = random.sample(data['faculties'], faculty_count)

        for faculty in faculties:
            profile += f"\n - {faculty}"

        # Append profile to results/results.txt
        with open('results/results.txt', 'a') as results:
            results.write(profile + "\n\n")
