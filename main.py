import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_excel


def get_manufacture_age(start_year):
    age = str(datetime.date.today().year - start_year)
    
    age_tens = '0' if len(age) <= 1 else age[-2]
    age_units = age[-1]
    measure = 'лет'
    if age_tens != '1':
        if age_units == '1':
            measure = 'год'
        elif age_units in '234':
            measure = 'года'

    return f'{age} {measure}'


def get_products_by_category(filepath):
    products_by_category = collections.defaultdict(list)
    production = read_excel(
        filepath, keep_default_na=False).to_dict(orient='records')
    for product in production:
        products_by_category[product['Категория']].append(product)
    return products_by_category


if __name__ == "__main__":
    start_year = 1920
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        winery_age=get_manufacture_age(start_year),
        drinks_by_category=get_products_by_category('wine.xlsx')
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
