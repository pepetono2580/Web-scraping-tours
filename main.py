import time

import requests
import selectorlib
import smtplib, ssl
import os


URL = "https://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "jrasgado01@gmail.com"
    password = "sncnvtontsziijbf"

    receiver = "jrasgado01@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

    print("Email was sent!")


def store(extraction):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")


def read(extract):
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == '__main__':
    while True:
        scraped = scrape(URL)

        extracted = extract(scraped)
        print(extracted)

        content = read(extracted)
        if extracted != "No upcoming tours":
            if extracted not in "data.txt":
                store(extracted)
                send_email("Hey, new event was found!")

        time.sleep(2)
