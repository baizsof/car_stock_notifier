import urllib.request
import urllib.parse
import re

def __parse_url_html(url):
    f = urllib.request.urlopen(url)
    return f.read().decode('utf-8')

def parse_cars(url):
    cars = []
    last_page_number = __parse_last_page_number(__parse_url_html(url))

    for i in range(1,last_page_number):
        current_page_html = __parse_page_html(url, i)
        current_cars = __parse_page_cars(current_page_html)
        cars.extend(current_cars)

    return cars

def __parse_last_page_number(html):
    page_number = re.search("(last.*?)(https.*?page)(\d+)", html).group(3)
    return  int(page_number)

def __parse_page_html(url, page_number):
    url += '/page' + str(page_number)
    return __parse_url_html(url)

def __parse_page_cars(html):
    cars = re.findall("contentId.*?(\d+)", html)
    return cars
