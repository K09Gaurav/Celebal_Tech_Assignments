import requests
import json
import schedule
import time
from datetime import datetime



## 1. Create a pipeline to fetch the 5 countries (india,us,uk,china,russia) data 
# from Rest API (https://restcountries.com/v3.1/name/{name} 
# here replace the {name} with Country name like https://restcountries.com/v3.1/name/us) 
# and save it in separate file as JSON with File name equal to Country name.

countries = ["india", "us", "uk", "china", "russia"]

def fetch():
    for country in countries:
        getdata = requests.get(f"https://restcountries.com/v3.1/name/{country}")
        if getdata.status_code == 200:
            data = getdata.json()

            with open(f"{country}.json", "w") as json_file:
                json.dump(data, json_file,indent=4)
                print(f"Data for {country} saved successfully.")
        else:
            print(f"Data for {country} Encountered an Error.")


## Add the trigger to above pipeline in such a way that 
# it will automatically run two times in a day ( 12:00 AM and 12:00 PM IST)

schedule.every().day.at("00:00").do(fetch)
schedule.every().day.at("12:00").do(fetch)
schedule.every().day.at("18:05").do(fetch)

while True:
    print("Checking For Pending Schedule")
    schedule.run_pending()
    time.sleep(60)


