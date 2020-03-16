import urllib.request
import urllib.parse
import re

def parse_cars(url):
    first_page_html = get_html(url)
    urls = [first_page_html, __parse_all_pages_url(first_page_html)]

    cars = []
    for url in urls:
        current_cars = __parse_page_cars(url)
        cars.extend(current_cars)

    return cars

def get_html(url):
    f = urllib.request.urlopen(url)
    return f.read().decode('utf-8')


def __parse_all_pages_url(html):
    urls = re.findall('(https:\/\/www\.hasznaltauto.hu\/talalatilista\/page.*?)"', html)
    return urls

def __parse_page_cars(url):
    html = get_html(url);
    cars = re.findall("contentId.*?(\d+)", html)
    return cars
