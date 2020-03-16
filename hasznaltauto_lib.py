import urllib.request
import urllib.parse
import re

def parse_cars(base_url):
    cars = []
    is_exit = False
    page = 1
    while is_exit == False:
        current_url = create_url(base_url, page)
        try:
            current_cars = __parse_page_cars(current_url)
            cars.extend(current_cars)
            page += 1
        except Exception:
            is_exit = True

    return cars

def create_url(base_url, page_number):
    return '{}/page{}'.format(base_url, page_number)

def __parse_page_cars(url):
    html = get_html(url);
    cars = re.findall("contentId.*?(\d+)", html)
    return cars

def get_html(url):
    f = urllib.request.urlopen(url)
    return f.read().decode('utf-8')
