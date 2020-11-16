import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
import csv


def main() -> None:
    url = starting_url
    print("Processing data")
    locations = find_locations(url)
    data = [final_data(location) for location in locations]
    file = ''.join([FILE, ".csv"])
    print(f"Writing data to file: {file}")
    csv_file(file, data)
    print(f"Data saved to file: {file}")


def extract_data(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")

    return soup


def find_tables(soup) -> list:
    return soup.find_all("table")


def find_locations(url) -> list:
    soup = extract_data(url)
    number = soup.find_all("td", {"class": "cislo"})
    url_p = "https://volby.cz/pls/ps2017nss/"

    return [[urljoin(url_p, x.find("a")["href"]), x.find("a").text] for x in number]


def final_data(locations: list) -> dict:
    url = locations[0]
    soup = extract_data(url)
    tables = find_tables(soup)
    data = {}

    try:
        data["CODE"] = locations[1]

        if len(soup.find_all("h3")) > 2:
            data["LOCATION"] = soup.find_all("h3")[2].text.split(": ")[1].strip("\n")
        else:
            data["LOCATION"] = soup.find_all("h3")[1].text.split(": ")[1].strip("\n")

        data["REGISTERED"] = tables[0].find_all("td")[3].text
        data["ENVELOPES"] = tables[0].find_all("td")[4].text
        data["VALID"] = tables[0].find_all("td")[7].text
        for x in [rows.find_all("td") for rows in tables[1].find_all("tr")[2:]]:
            data[x[1].text] = x[2].text
        for y in [rows.find_all("td") for rows in tables[2].find_all("tr")[2:]]:
            data[y[1].text] = y[2].text

        return data

    except AttributeError:
        print("Incorrect indexes")


def csv_file(file, data):
    with open(file, "a", newline="") as csv_s:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csv_s, fieldnames=fieldnames)
        writer.writeheader()

        for row_dict in data:
            writer.writerow(row_dict)


if __name__ == "__main__":
    try:
        starting_url = sys.argv[1]
        FILE = sys.argv[2]
    except IndexError:
        print("You can write url address and name of the file")
        sys.exit()
    main()
