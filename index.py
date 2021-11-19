# Import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import json

# Download chromedriver using ChromeDriverManager.
# This is supposedly better than manually specifying the path since it's already deprecated.
driver = webdriver.Chrome(ChromeDriverManager().install())

# Delete all text in results/results.txt
with open("results/results.txt", "w") as f:
    f.write("")

university_count = 1

# Parse data/data.json
with open('data/data.json') as json_file:
    data = json.load(json_file)

    print(f"Processing {len(data['universities'])} university(s)..")

    # Loop over all universities
    for university in data['universities']:
        result = f"{university_count}. {university['name']}\n\n"

        # Open the quipper website
        driver.get(university['quipper'])

        profile_div = driver.find_element(By.CLASS_NAME, 'school-profile__description')
        profile = profile_div.find_element(By.TAG_NAME, 'p').get_attribute('innerHTML')
        result += f"Profil:\n{profile}\n\n"

        result += "Fakultas:\n"
        faculties_div = driver.find_element(By.CLASS_NAME, 'school-faculties__list')
        for faculty in faculties_div.find_elements(By.TAG_NAME, 'a'):
            faculty_name = faculty.find_element(By.CLASS_NAME, 'faculty-item__name').get_attribute('innerHTML')
            result += f"{faculty_name}\n"

        result += "\n"

        # The admission table we want is the first table element in the page so dw
        try:
            admission_table = driver.find_element(By.TAG_NAME, 'table')
            admission_tbody = admission_table.find_element(By.TAG_NAME, 'tbody')
            # Admission method is also the first (and only) ol in the table
            admission_tr = admission_table.find_elements(By.TAG_NAME, 'tr')[1]
            admission_method = admission_tr.find_element(By.TAG_NAME, 'td').get_attribute('innerText')
            result += f"Jalur masuk:\n{admission_method}\n\n"
            # print(admission_method)
        except NoSuchElementException:
            print(f"No admission table for university {university['name']}")

        print(result)

        # Write the results to results/results.txt
        with open("results/results.txt", "a") as f:
            f.write(result)

        print(f"Finished processing {university['name']} ({university_count})")

        university_count += 1
