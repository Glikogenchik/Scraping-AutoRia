import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time


def get_bmw():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", 'accept': '*/*'
    }
    
    url = "https://auto.ria.com/newauto/marka-bmw/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    propositions = soup.find_all("section", class_="proposition")


    cars_dict = {}
    for proposition in propositions:
        proposition_title = proposition.find("div", class_="proposition_title").text.strip()
        proposition_url = f'https://auto.ria.com{proposition.get("href")}'

        proposition_date_time = proposition.find("time").get("datetime")
        date_from_iso = datetime.fromisoformat(proposition_date_time)
        date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
        proposition_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())

        proposition_id = proposition_url.split("/")[-1]
        proposition_id = proposition_id[:-4]

        # print(f'{proposition_title} | {proposition_url}')

        cars_dict[proposition_id] = {
            "proposition_date_timestamp": proposition_date_timestamp,
            "proposition_title": proposition_title,
            "proposition_url": proposition_url
        }

    with open("cars_dict.json", "w") as file:
        json.dump(cars_dict, file, indent=4, ensure_ascii=False)


def chek_cars_update():
    with open("cars_dict.json") as file:
        cars_dict = json.load(file)

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", 'accept': '*/*'
    }
    
    url = "https://auto.ria.com/newauto/marka-bmw/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    propositions = soup.find_all("section", class_="proposition  ")

    fresh_cars = {}
    for proposition in propositions:
        proposition_url = f'https://auto.ria.com{proposition.get("href")}'
        proposition_id = proposition_url.split("/")[-1]
        proposition_id = proposition_id[:-4]

        if proposition_id in cars_dict:
            continue
        else:
            proposition_title = proposition.find("section", class_="proposition_title").text.strip()
        
            proposition_date_time = proposition.find("time").get("datetime")
            date_from_iso = datetime.fromisoformat(proposition_date_time)
            date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
            proposition_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())

            cars_dict[proposition_id] = {
            "proposition_date_timestamp": proposition_date_timestamp,
            "proposition_title": proposition_title,
            "proposition_url": proposition_url
        }
    
    with open("cars_dict.json", "w") as file:
        json.dump(cars_dict, file, indent=4, ensure_ascii=False)
    
    return fresh_cars


    
def main():
    #get_bmw()
    print(chek_cars_update())


if __name__ == '__main__':
    main()
    