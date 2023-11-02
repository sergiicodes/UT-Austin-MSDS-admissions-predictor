# Import Dependencies 
from selenium import webdriver
import json
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_data_from_page(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id$=comment-rtjson-content]')))
    posts = driver.find_elements(By.CSS_SELECTOR, 'div[id$=comment-rtjson-content]')

    print(f"Found {len(posts)} posts on {driver.current_url}") # Debugging line

    data_list = []
    for post in posts:
        data_dict = {}
        fields = post.find_elements(By.TAG_NAME, 'p')

        for field in fields:
            split_data = field.text.split(":")
            if len(split_data) > 1:
                key = split_data[0].strip().lower().replace(':', '').replace('.', '').replace(' ', '')
                value = ':'.join(split_data[1:]).strip()
                data_dict[key] = value
        data_list.append(data_dict)
    
    return data_list


# All of the subreddits 
urls = [
        
    # Fall 2021
    'https://www.reddit.com/r/MSDSO/comments/k6w42u/fall_2021_admissions_thread/',
        
    # Spring 2021
    'https://www.reddit.com/r/MSDSO/comments/imrys0/spring_2021_admissions_thread/', 
        
    # Fall 2022
    'https://www.reddit.com/r/MSDSO/comments/sxewtz/fall_2022_admissions_thread/', 
        
    # Spring 2022
    'https://www.reddit.com/r/MSDSO/comments/nxburi/spring_2022_admissions_thread/', 
    
    # Fall 2023
    'https://www.reddit.com/r/MSDSO/comments/13x3v2m/fall_2023_admissions_thread/',
    
    # Spring 2023
    'https://www.reddit.com/r/MSDSO/comments/wpp70y/spring_2023_admission_thread/',
    
    # Spring 2024
    'https://www.reddit.com/r/MSDSO/comments/148pyv5/spring_2024_admission_thread/',
]

all_data = []

options = webdriver.ChromeOptions()
# Uncomment below line if you want Chrome to run in headless mode
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

for url in urls:
    driver.get(url)
    extracted_data = extract_data_from_page(driver)
    all_data.extend(extracted_data)
    time.sleep(5)  # 5-second delay between each URL

driver.close()

# Save the extracted data to a JSON file
with open('all_data.json', 'w') as outfile:
    json.dump(all_data, outfile)
